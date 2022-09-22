from symbol import parameters
import pandas as pd
import pickle
import pika
import time 
import os

data = pd.read_csv('sampledat.csv')

parameters = pika.URLParameters(os.environ['AMQP_URL'])
connection = pika.BlockingConnection(parameters=parameters)
channel = connection.channel()
channel.exchange_declare(exchange='fraudDetection',exchange_type='direct')


for i in range(len(data)):
    serialized = pickle.dumps({'row':data.iloc[i]})
    channel.basic_publish(exchange='fraudDetection',routing_key='CreditCardData', body=serialized)
    print(f"Publishing Transaction #{i}")
    time.sleep(2)