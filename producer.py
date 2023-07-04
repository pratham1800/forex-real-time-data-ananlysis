from kafka import KafkaProducer
import requests
from json import dumps
import time


kafka_data_producers = KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=(0,11,5),value_serializer=lambda x: dumps(x).encode('utf-8') )


while True:
    response_data = requests.get("https://api.tiingo.com/tiingo/fx/top?tickers=audusd,eurusd&token=2a57ade51bed6fb489af8358db234d6306fc083f")
   
     
    data = {'Lagos' : response_data.json()}
    data=data['Lagos'][0]
    kafka_data_producers.send('project3', value=data)
   
    print(data)
    time.sleep(30)
    
    
    
