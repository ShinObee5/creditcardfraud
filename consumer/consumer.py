import pickle
from venv import create
import pika, sys, os
import time
import pandas as pd
import sys
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.orm import sessionmaker
from xgboost import XGBClassifier
from model import Base, Transaction

# Declaring Global Variables
model=''
s=''

def connect_to_queue():
    connection=""
    while(not connection):
        try:
            connection = pika.BlockingConnection(pika.URLParameters(os.environ.get('RABBITMQ_URL')))
        except:
            print(f"Trying to Establish Connection to RabbitMQ {connection}")
            time.sleep(10)
    return connection

def make_session():
    engine=""
    while(not engine):
        try:
            engine = create_engine(os.environ.get('POSTGRESQL_URL'))
            # Creating Database If Not Exists
            if not database_exists(engine.url):
                create_database(engine.url)
        except:
            print(f"Trying to Connect to DB {engine}")
            time.sleep(10)
    try:
        if sys.argv[1]=='--restart':
            Base.metadata.drop_all(engine)
    except IndexError:
        pass
    except:
        print("Error Cleaning DB")
    Base.metadata.create_all(engine)
    Session=sessionmaker(bind=engine)
    s = Session()
    return s

def callback(ch, method, properties, body):
            global s
            unserialized=pickle.loads(body)
            single_row = pd.DataFrame(unserialized['row']).T
            t = Transaction(time=int(single_row['Time']), amount=float(single_row['Amount']))
            try:
                single_row.drop(['Amount','Class'],axis=1,inplace=True)
            except Exception as e:
                print(f"Error {e} while dropping columns")
            answer=model.predict(single_row)[0]
            t.Class=int(answer)
            s.add(t)
            s.commit()

def main():
        # Get DB Session
        global s
        s = make_session()

        #Connect to Queue
        connection = connect_to_queue()
        
        # Declaring Exchanges and Bindings
        channel = connection.channel()
        channel.queue_declare('CreditCardData')
        channel.exchange_declare(exchange='fraudDetection',exchange_type='direct')
        channel.queue_bind('CreditCardData','fraudDetection','CreditCardData')

        # Consuming
        channel.basic_consume(queue='CreditCardData', on_message_callback=callback, auto_ack=True)
        print('Consumer Starting.......[*]')
        channel.start_consuming()

if __name__ == '__main__':
    try:
        #Loading Pickled XGBoost Model
        with open('model.pkl','rb') as f:
            model = pickle.load(f)
        
        #Main Function
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)