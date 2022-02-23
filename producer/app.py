from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
import time
import random

print(1)

producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda m: json.dumps(m).encode('ascii'))

for i in range(2):
    for symbol in ('AAA', 'ZZZ'):
        
        stock = {'symbol': symbol, 'price': random.random()*100}
        print('Producing:', stock)
        
        future = producer.send('market.prices', stock)
        record_metadata = future.get(timeout=10)
        time.sleep(3)

# print (record_metadata.topic)
# print (record_metadata.partition)
# print (record_metadata.offset)

# while True:
#     stock = {'SYMBOL': random.random()*100}
#     producer.send('price-topic', stock)
#     print(stock)
#     time.sleep(1)

