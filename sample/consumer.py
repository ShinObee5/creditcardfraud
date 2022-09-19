import pickle
import pika, sys, os
import time
from sample_model_creator import Model

def main():
        credentials = pika.PlainCredentials('adi', 'adi')
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',port=5672,credentials=credentials))
        channel = connection.channel()
        channel.queue_declare('CreditCardData')
        channel.exchange_declare(exchange='fraudDetection',exchange_type='direct')
        channel.queue_bind('CreditCardData','fraudDetection','CreditCardData')
        with open('sample//model.pkl','rb') as f:
            model = pickle.load(f)
        def callback(ch, method, properties, body):
            unserialized=pickle.loads(body)
            print(f' Input: {unserialized} \n Predicted Value = {model.predict(body)}')
            time.sleep(5)
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