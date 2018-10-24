from kafka import KafkaProducer
import json, time

# Configure address, port, kafka topic, and file name
osaIP = '129.146.151.215'
kafkaPort = '9092'
address = osaIP + ':' + kafkaPort
topic = 'demo'
dataFile = 'iotData.json'

# Create kafka producer
producer = KafkaProducer(bootstrap_servers=[address], api_version=(0,10))

# Open data file, iterate through data and send a value to kafka every 2 seconds
with open(dataFile, 'r') as jsonFile:

    data = json.load(jsonFile)
        
    for item in data:

        payload = json.dumps(item).encode('utf-8')
        producer.send(topic, payload)

        print ('SEND: ' + str(payload))
        time.sleep(2)