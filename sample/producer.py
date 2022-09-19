import pandas as pd
import pickle
import pika
import time 
import os

data = pd.read_csv('sample//sampledat.csv')

credentials = pika.PlainCredentials('adi', 'adi')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',port=5672,credentials=credentials))
channel = connection.channel()
channel.exchange_declare(exchange='fraudDetection',exchange_type='direct')


for i in range(len(data)):
    print(data.loc[i,])
    serialized = pickle.dumps({'row':data.loc[i,]})
    channel.basic_publish(exchange='fraudDetection',routing_key='CreditCardData', body=serialized)
    time.sleep(2)