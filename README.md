# OSA Kafka Demo
This is a simple walkthrough to get started streaming data to Oracle Stream Analytics (OSA) on Ravello with Kafka and Python.  For the purposes of the walkthrough, the data is streamed from a local file of synthesised IoT sensor data.  After this walkthrough, the same process with Kafka, Python, and OSA can be used with other data sources.  This will be addressed in the 'Next Steps' section of this document.

## Getting Started
These instruciton will explain the steps necessary to stream data into OSA on Ravello.  This method uses Kafka and Python, along with a sample dataset.  Make sure you have all of the prerequisites, and refer to the system architecture as needed.

### Prerequisites
* Ravello Account
* Ravello "OSA OGG Demo" Blueprint
* Python 2.7
* kafka-python module

Installing kafka-python:
```
pip install kafka-python
```

### System Architecture
![image](https://user-images.githubusercontent.com/42782692/47517279-8cff9e80-d83c-11e8-96ec-6c76bd360e0a.png)

## Setting Up Ravello for OSA
If you have access to the Oracle Ravello "OSA OGG Demo" Blueprint, follow the steps below to configure the blueprint for use with the rest of this walkthrough.

### Initialize the Ravello Application
Once the blueprint is in your library, click "Create Application" and provide a different name if desired.  Locate this new application in the applications menu, and click "Publish".  

### Configure the Application's NIC
After publishing your application, the NIC configuration should be changed to use an elastic IP address.  To do this, click on the application bock in the canvas to open the menu on the right side of the screen.  Select the header that says "NICs" and click "Open" on the DHCP section.  Click "Elastic IP", then click "Select".  In the pop-up window, click "Create Elastic IP Address" and select the appropriate region.  Check the box for the new IP address to select it, then click "Select" at the botttom of the window.  Click "Save" in the menu on the right, and then update the application with "Update" at the top of the canvas.  This will ensure that the application uses the same IP address every time it restarts.

### Run the OSA Application
Click the "Start" button on the bottom of the menu on the right, and select how long you want the application to run.  It will take aproximately 5 minutes for the application to show that it is running, and about 5 more after that to be able to access OSA.  Also take note of the port numbers in the summary section of the menu on the right side of the screen.  Those will be used later on in Python and OSA.

## Creating a Kafka Topic
Each data stream in OSA requires a designated Kafka topic.  These are created in OSA via SSH.

### SSH into the OSA Instance
Click on the blue "Application Documentation" icon in the top menu bar of the application canvas on Ravello.  Take note of the username and password for SSH access to OSA.  SSH into the OSA instance using that username and password, along with the public IP address of the OSA instance.

```
ssh [username]@[public IP]
[enter password]
```

### Create Kafka Topic
Once you are in the OSA instance via SSH, use the "kcreate" command to create a Kafka topic.

```
kcreate [topic name]
```

There should be a success message, after which you can exit out of the SSH connection.

## Streaming to Kafka with Python
The Python script kafkaStream.py and your machine's hosts file need some configuration in order to stream data into the OSA Kafka topic.

### Configure Python Script
In kafkaStream.py, lines 6 and 12 need configuration based on your system. In line 6, you must set "osaIP" equal to your OSA public IP address.  This value needs to be in quotations.

```
osaIP = 'x.x.x.x'
```

In line 12, set "topic" equal to the name of the Kafka topic you created.  This also must be in quotations.

```
topic = 'your_kafka_topic_name'
```

The "kafkaPort" value is set based on the Ravello blueprint, but needs to be updated if you change your port numbers.  Similarly, if you use a different data file, "dataFile" needs to be updated accordingly.

### Configure Hosts File
In order for the Python script to connect with Kafka, you need to update the hosts file in /etc on your computer.  This will provide the proper IP address for the Kafka connection.

Start by navigating to the file's directory.

```
cd /etc
```

Open hosts for editing with sudo, as the file is read only.

```
sudo vim hosts
```

The file will have several lines with IP addresses followed by their names.  You need to add an entry at the end of the list with the OSA public IP address, followed by "osacs".

To do this, press "i" to insert text.  Navigate to the last entry with the arrow keys, and press "return" to enter a new line.  Type the following, being sure to match the formatting of the other entries.

The new entry should look like this:

```
[your OSA IP] osacs
```

To save and exit the file, press "escape" followed by ":wq".  You can check that the file has been written correctly with the following command:

```
cat hosts
```

The Python script is now configured to connect properly with OSA.

### Key Points
There are a couple key functions to take note of in the kafkaStream.py.  In line 16, we define a Kafka producer.  This establishes a connection with the OSA instance, so that we can then send data to Kafka topics within OSA.

In line 25, we send data to a specific Kafka topic using the Kafka producer that we have already created.  In future projects, you can send data from different sources and in different ways depending on your needs by building around these two commands.

## Setting Up OSA

### Create a Connection

### Create a Stream

### Create a Pipeline

### Create a Dashboard

## Next Steps