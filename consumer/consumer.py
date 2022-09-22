import pickle
import pika, sys, os
import time
import pandas as pd
from xgboost import XGBClassifier
COUNT=0
def main():
        parameters = pika.URLParameters(os.environ['AMQP_URL'])
        connection = pika.BlockingConnection(parameters=parameters)
        channel = connection.channel()
        channel.queue_declare('CreditCardData')
        channel.exchange_declare(exchange='fraudDetection',exchange_type='direct')
        channel.queue_bind('CreditCardData','fraudDetection','CreditCardData')
        with open('model.pkl','rb') as f:
            model = pickle.load(f)
        def callback(ch, method, properties, body):
            global COUNT
            unserialized=pickle.loads(body)
            single_row = pd.DataFrame(unserialized['row']).T
            try:
                single_row.drop(['Amount','Class'],axis=1,inplace=True)
            except Exception as e:
                print(f"Error {e} while dropping columns")
            answer=model.predict(single_row)[0]
            status = 'Legit' if answer else 'Fraud'
            print(f"Transaction #{COUNT} is {status}")
            COUNT+=1

        channel.basic_consume(queue='CreditCardData', on_message_callback=callback, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)