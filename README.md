# OSA Kafka Demo
This is a simple walkthrough to get started streaming data to Oracle Stream Analytics (OSA) on Ravello with Kafka and Python.  For the purposes of the walkthrough, the data is streamed from a local file of synthesised IoT sensor data.  After this walkthrough, the same process with Kafka, Python, and OSA can be used with other data sources.  This will be addressed in the 'Next Steps' section of this document.

## Getting Started
These instruciton will explain the steps necessary to stream data into OSA on Ravello.  This method uses Kafka and Python, along with a sample dataset.  Make sure you have all of the prerequisites, and refer to the system architecture as needed.

### Prerequisites
* Ravello Account
* Ravello "OSA OGG Demo" Blueprint
* Python 2.7 or later
* kafka-python module

Installing kafka-python:
```
sudo pip install kafka-python
```

### File Structure
For the demo to run successfully, make sure that the provided data file "iotData.json" is in the same directory level as the python script "kafkaStream.py".  If this is changed, you will have to edit the python script to reflect your changes.

### System Architecture
![image](https://user-images.githubusercontent.com/42782692/47517279-8cff9e80-d83c-11e8-96ec-6c76bd360e0a.png)

## Setting Up Ravello for OSA
If someone has shared access to the Oracle Ravello "OSA OGG Demo" Blueprint with you, follow the steps below to configure the blueprint for use with the rest of this walkthrough.

### Initialize the Ravello Application
In Ravello, click "Library", then click "Blueprints".  Click the "Shared with Me" button in the top right of the page, and click on the "OSA OGG Demo" blueprint.  Now click the orange "Copy to My Blueprints" button, then navigate back to your blueprint library and click on your new blueprint.  Click "Create Application" and provide a different name if desired.  Locate this new application in the applications menu, and click "Publish".  

### Configure the Application's NIC
After publishing your application, the NIC configuration should be changed to use an elastic IP address.  To do this, click on the application bock in the canvas to open the menu on the right side of the screen.  Select the header that says "NICs" and click "Open" on the DHCP section.  Click "Elastic IP", then click "Select".  In the pop-up window, click "Create Elastic IP Address" and select the appropriate region.  Check the box for the new IP address to select it, then click "Select" at the bottom of the window.  Click "Save" in the menu on the right, and then update the application with "Update" at the top of the canvas.  This will ensure that the application uses the same IP address every time it restarts.

### Run the OSA Application
Click the "Start" button on the bottom of the menu on the right, and select how long you want the application to run.  It will take aproximately 5 minutes for the application to show that it is running, and about 5 more after that to be able to access OSA.  Also take note of the elastic IP address and port numbers in the summary section of the menu on the right side of the screen.  Those will be used later on in Python and OSA.

## Creating a Kafka Topic
Each data stream in OSA requires a designated Kafka topic.  These are created in OSA via SSH.

### SSH into the OSA Instance
Click on the blue "Application Documentation" icon in the top menu bar of the application canvas on Ravello.  The location of this icon is shown in the screenshot below.

![image](https://user-images.githubusercontent.com/42782692/47528304-b24ed580-d859-11e8-8394-3ad8e9ff13e3.png)

Take note of the username and password for SSH access to OSA.  SSH into the OSA instance using that username and password, along with the public IP address of the OSA instance.

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

Start by opening your command line on your local computer and navigating to the file's directory.

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
Now that Ravello, Python, and your local machine are configured, the next step is accessing OSA in your browser and setting up the data stream.

### Access OSA
To access the OSA interface, you will need the OSA public IP address and the OSA port number found in the summary tab of the Ravello application menu.  Make sure you are not on a network that will block your connection (e.g. clear corporate), then navigate to the following address in your browser:

```
[OSA public IP]:[OSA port number]/osa
```

This should direct you to a login page, where you should enter the username and password provided by clicking on the blue "Application Documentation" icon in the top menu bar of the application canvas in Ravello.

At this point, you have completed the configuration and initial setup for OSA with Kafka and Python.  The following sections will walk you through some simple actions in OSA to get you started, but the real power of OSA will be when you explore OSA's capabilities to create innovative solutions.

### Create a Connection
Connections link to Kafka topics, and allow you to access the data that Python is sending to Kafka.  Navigate to the "Catalog" tab in the top right corner of OSA.  This is where most of your OSA work will occur.  Click the green "Create New Item" button and select "Connection" from the drop-down menu.

Enter a name for the connection, a description and tags if desired, and then select "Kafka" for the connection type.  Click next.

In "Connection Details", enter the OSA public IP address followed by the port number for Zookeeper.  The zookeeper port number is found in the summary tab of the right-hand menu of Ravello, in the blue box by the start and stop buttons.  You might have to scroll down in the box to find it.

```
[OSA public IP]:[zookeeper port number]
```

Click "Test Connection" to ensure that the connection is successful, then click "Save".

### Create a Stream
Now that you have a connection to your Kafka topic, you need to create a stream for the data.  In the catalog, click "Create New Item" and select "Stream" from the drop-down menu.

Give your stream a name, a description and tags if desired, and select "Kafka" as the stream type.  Leave "Create Pipeline with this source" unchecked.  We will do that in the next step.  Click "Next".

In "Source Details" select your the connection you just created, and select the topic name that corresponds to the Kafka topic you created via SSH.  For this demo, set the Data Format to JSON, as that matches the provided data set.  Click "Next".

In "Data Format" check both "Allow missing column names" and "Array in Multi-lines", and then stop.  Read the next step before clicking "Next".

The "Shape" tab in stream creation will infer the headers and data types for the data streaming into your Kafka topic.  Because of this, you must start the kafkaStream.py script before advancing to the "Shape" tab, so that there is data streaming in the Kafka topic for OSA to infer from.  The python script will send a new data point every 2 seconds until the entire file is sent.  This will take 2 hours, but then you will need to restart kafkaStream.py if you wish to keep working.

Start kafkaStream.py

```
python kafkaStream.py
```

While kafkaSream is running, that terminal window will print a new data point that it has sent to the Kafka topic every 2 seconds.

Now that Python is streaming data into the Kafka topic, return to the OSA "Create Stream" window and click "Next" to advance to the "Shape" tab.  Wait for OSA to infer the data.  When it completes, you will see field names and field paths corresponding to the data at the bottom of the window.

At this point, click on "Manual Shape" to edit the field names and field types.  Field names like "Date" and "Time" are reserved by OSA as key words, so change the field names of those entries to "CurrentDate" and "CurrentTime" respectively.  Make sure to leave the field paths unchanged.

Change the field type of Temperature, Light, and Humidity to "Number".  Change the CurrentTime field type to "Timestamp".  Leave CurrentDate as "Text", and change DateTime to "Big Integer".  Click to clock icon next to DateTime to set that field as the timestamp.  Click "Save".

### Create a Pipeline
Pipelines allow you to work with the data points (events) in the data stream, filtering or processing the events as needed.  In the OSA catalog, click "Create New Item" and select "Pipeline" from the drop-down menu.  Give the pipeline a name, a description and tags as desired, and select your recently created stream from the "Stream" drop-down.  Click "Save".  This will open the pipeline editor.  Wait for the "Live Output" window to finish "Starting Pipeline", and then you should see data points streaming in from kafkaStream.py.

At this point you are ready to work with your real-time streaming data.

### Stages and Visualizations
The pipeline editor initially only shows your stream, where all your data is streaming in as events.  Stages allow you to process these events in various ways.

To create a stage, right-click on the stream in the pipeline editor, and hover over "Add a Stage", then select the desired stage for your data.  For a simple example with the provided IoT data, select "Query" and name the query stage "Temperature Filter".  With the Temperature Filter icon selected, click on the "Filters" tab in the editor on the right of the screen and then click "Add a Filter".  

Make sure that "Match All" is selected.  In the "Select a field" drop-down menu, select "Temperature", and in "Select an operator" select "greater than".  In the "Enter a value" text box, type 72, or another temperature threshold value if you prefer.  Click in the white space outside of the filter parameters to stop editing the filter.  Now, if the Temperature Filter icon is selected in the block diagram, the "Live Output" window will display only events where the temperature exceeds the threshold in the filter.  This output can be sent to other destinations using targets, which will be described in the next section.

To create a simple visualization, right click on the stream, hover over "Add a Stage", and select "Rule".  Name the rule stage "Temperature Visual" and give it a description if desired.  In the "Rules" tab of the rule editor, name the rule "Visual" and click "Done".  Next, in the "IF" section of the rule, make sure "Match All" is selected, and click "Add a Condition".  Choose "Temperature" for "Select a field", and choose "is not null" for "Select and operator", scrolling down in the menu if necessary.

Next, click "Add Action" in the "THEN" section.  In the "Select a field" drop-down choose "Temperature", and in the expression text box type "=Temperature" and click the "Temperature" field that populates under the text box.  All that this rule does is pass all valid temperature values through to our visualization.  Click in the white space outside of the rule parameters to stop editing the rule.

After creating the rule, click the "Visualizations" tab in the rule stage editor, click "Add a Visualization", and select "Line Chart".  In the pop-up window name your chart "TemperatureChart" and give it a description and tags if desired.  Set the "Y Axis Field Selection" to "Temperature" by clicking the plus sign next to "Specify Value".  Label the Y axis "Temperature" in the "Axis Label" text box.  Use the "X Axis Field Selection" drop-down to select "DateTime" as the X axis value.  Set the X axis label to "Time".  Leave "Horizontal" unchecked for "Orientation", and leave "Data Series Selection" blank.  Finally, click "Create".  You can view this visualization in real-time in the "Visualizations" tab of the "Temperature Visual" rule stage, or in a dashboard as described in a following section.

### Create Targets
Targets allow specific OSA events to trigger other actions.  By right-clicking on the final stage in a stream, you can add a target stage.  Targets are outside the scope of this walkthrough, but targets can have connection types such as Kafka, CSV File, REST, and much more, depending on your implementation needs.  The Oracle Stream Analytics official documentation has more information on Targets.

### Create a Dashboard
Dashboards allow you to view multiple visualizations on one screen.  However, before creating a dashboard you need to publish any pipelines that have visualizations you want to include.  For this demo, publish your pipeline by clicking "Publish" in the top right corner of the screen.  Leave all values as default on the publishing window, and click "Publish"  This will prevent any additional changes to your pipeline, though you can unpublish at any time if edits are needed.

Click "Done" in the top left of the screen to return to the catalog.  Now click "Create New Item" and select "Dashboard" from the drop-down menu.  Give your dashboard a name, and provide a description and tags if desired.  Click "Next".  Leave CSS blank, and click "Save".  Click on your new dashboard in the catalog to open it.

The dasboard tools are at the top right corner of the new dashboard.  Click the plus icon, then navigate the visualization list and check the box next to "TemperatureChart" or any other visualizations you may have created.  These may appear on the second page of the list.  Click "Add Visualizations"  Once added, click the save icon in the dashboard to save the current state of the dashboard for future use.

## Next Steps
You have now successfully connected OSA, Kafka, and Python for streaming demo data.  With all of this complete, the next steps are to expand on this foundation and implement solutions for actual use cases.  While this demo uses sample data in the form of a local json file, you can redesign the data source in Python to fit your solution using the two key Python commands described in the "Key Points" section of this documentation.  

For example, the Python script could make the Kafka producer, then run an infinite loop that pulls data from an IoT device and sends it to a Kafka topic.  Another example involves the Python script using API calls to retrieve data from another source, then sending the data to a Kafka topic.  Additionally, it is important to note that you can send data to multiple Kafka topics in the same script, which can be valuable depending on your solution implementation.  For additional information on OSA capabilities, refer to the official [Oracle Stream Analytics documentation](https://docs.oracle.com/middleware/1221/osa/using-streamanalytics/toc.htm).