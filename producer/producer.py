from multiprocessing import connection
import pandas as pd
import pickle
import pika
import time 
import os

data = pd.read_csv('sampledat.csv')

def connect_to_queue():
    connection=""
    while(not connection):
        try:
            connection = pika.BlockingConnection(pika.URLParameters(os.environ.get('RABBITMQ_URL')))
        except:
            print(f"Trying to Establish Connection to RabbitMQ {connection}")
            time.sleep(10)
    return connection


connection = connect_to_queue()

channel = connection.channel()
channel.queue_declare('CreditCardData')
channel.exchange_declare(exchange='fraudDetection',exchange_type='direct')
channel.queue_bind('CreditCardData','fraudDetection','CreditCardData')

for i in range(len(data)):
    serialized = pickle.dumps({'row':data.iloc[i]})
    channel.basic_publish(exchange='fraudDetection',routing_key='CreditCardData', body=serialized)
    print(f"Publishing Transaction #{i}")
    time.sleep(5)