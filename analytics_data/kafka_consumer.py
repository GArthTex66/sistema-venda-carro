from confluent_kafka import Consumer
from models.connection_options.kafka_configs import kafka_infos
from .save_analytic_service import SaveAnalyticService

consumer = Consumer(kafka_infos)

print('Kafka Consumer has been initiated...')

print('Available topics to consume: ', consumer.list_topics().topics)
consumer.subscribe(['car-post-topic'])

def main():
    while True:
        msg = consumer.poll(1.0) #timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data = msg.value().decode('utf-8')
        print(data)
        SaveAnalyticService().saveDataAnalytics(data)     
    consumer.close()

if __name__ == '__main__':
    main()

