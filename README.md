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

### Initializing the Ravello Application
Once the blueprint is in your library, click "Create Application" and provide a different name if desired.  Locate this new application in the applications menu, and click "Publish".  

### Configuring the Application's NIC
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

## Setting Up OSA

### Creating a Connection

### Creating a Stream

### Creating a Pipeline

### Creating a Dashboard

## Next Steps