from kafka import KafkaProducer
import json, time

# Configure IP, port, and format address
# Replace osaIP with your OSA IP address
osaIP = '129.146.151.215'
kafkaPort = '9092'
address = osaIP + ':' + kafkaPort

# Set name of Kafka topic for sending data, and set file name for the data
topic = 'demo'
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