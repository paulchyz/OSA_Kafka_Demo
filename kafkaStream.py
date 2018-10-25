from kafka import KafkaProducer
import json, time

# Configure IP, port, and format address
# Insert your OSA IP in quotations (Example: osaIP = 'x.x.x.x')
osaIP = 'your_OSA_IP'
kafkaPort = '9092'
address = osaIP + ':' + kafkaPort

# Set name of Kafka topic for sending data, and set file name for the data
# Insert your Kafka topic name in quotations (Example: topic = 'demo')
topic = 'your_kafka_topic_name'
dataFile = 'iotData.json'

# Create a kafka producer
producer = KafkaProducer(bootstrap_servers=[address], api_version=(0,10))

# Open the local data file and load into python object
with open(dataFile, 'r') as jsonFile:
    data = json.load(jsonFile)
    
    # Iterate through the data, dump into json object with proper encoding, and send to Kafka topic
    for item in data:
        payload = json.dumps(item).encode('utf-8')
        producer.send(topic, payload)

        # Terminal output and 2 second delay
        print ('SEND: ' + str(payload))
        time.sleep(2)