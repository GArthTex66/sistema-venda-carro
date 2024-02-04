from confluent_kafka import Consumer

consumer = Consumer({'bootstrap.servers':'localhost:9092','group.id':'analytics-posts-group','auto.offset.reset':'earliest'})

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
    consumer.close()

if __name__ == '__main__':
    main()

