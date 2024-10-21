# MQTT Pub-Sub Model for Sensor Data Collection

## Project Overview
This project demonstrates an MQTT-based publish-subscribe (pub-sub) model for sensor data collection. It uses a **Raspberry Pi 3** as a data producer to collect sensor readings (temperature and humidity) from a **DHT11** sensor. The data is sent to an **MQTT broker** running on an **Ubuntu machine**, and subscribers (also on Ubuntu) receive and process the sensor data. The project aims to showcase IoT data transmission using the MQTT protocol, emphasizing its lightweight and efficient communication model.

## Table of Contents
- [Project Overview](#project-overview)
- [System Architecture](#system-architecture)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
  - [Installing Dependencies](#installing-dependencies)
  - [Configuring the Raspberry Pi (Publisher)](#configuring-the-raspberry-pi-publisher)
  - [Configuring the Broker (Ubuntu)](#configuring-the-broker-ubuntu)
  - [Configuring the Subscriber (Ubuntu)](#configuring-the-subscriber-ubuntu)
- [MQTT Pub-Sub Workflow](#mqtt-pub-sub-workflow)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## System Architecture

### Components:
1. **Producer (Publisher)**: Raspberry Pi 3 reads sensor data from the DHT11 sensor and publishes it to the MQTT broker.
2. **Broker**: The MQTT broker (Mosquitto) is hosted on an Ubuntu machine. It facilitates communication between the publisher and subscribers.
3. **Subscriber**: One or more Ubuntu machines subscribe to the broker and receive the sensor data to process or display.

### Diagram:
```text
+----------------+       +------------------+       +----------------+
|   Publisher    | --->  |     MQTT Broker   | --->  |   Subscriber   |
| Raspberry Pi 3 |       |      (Ubuntu)     |       |    (Ubuntu)    |
|  (DHT11 data)  |       |    Mosquitto      |       |   Process data |
+----------------+       +------------------+       +----------------+
```
## Requirements
### Hardware:
- Raspberry Pi 3 (with Raspbian OS)
- DHT11 Sensor
- Ubuntu machines (for the broker and subscriber)

### Software:
- Python 3.x
- `paho-mqtt` version 2.1.0 for MQTT protocol
- DHT11 Python library (for sensor readings)
- `mosquitto` MQTT broker (on Ubuntu)

## Setup Instructions

### 1. Install MQTT Broker (Mosquitto) on Ubuntu
```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```
### 2. Install Required Libraries on Raspberry Pi
```bash
sudo apt update
sudo apt install python3-pip
pip3 install paho-mqtt
pip3 install Adafruit_DHT
```
### 3. Publisher Setup (Raspberry Pi 3)
- Connect the DHT11 sensor to the Raspberry Pi GPIO pins.
- Use the Adafruit_DHT library to read sensor data.
- Publish the data to the MQTT broker.

### 4. Refer to the 
```bash
producer.py
```
and 
```bash
subscriber.py
```
for the codes.

### 5. Run the Project
 Start the Mosquitto broker on the Ubuntu machine by running:

```bash

sudo systemctl start mosquitto
```
Run the publisher on Raspberry Pi:

```bash

python3 publisher.py
```
Run the subscriber on another Ubuntu machine:

```bash

python3 subscriber.py
```


#### FOR THE IN-DEPTH UNDERSTANDING REFER TO THE [PDF ADDED](https://github.com/pranay-patle/MQTT-Pub-Sub-Model-for-Sensor-Data-Collection/blob/main/Mqtt_pub_sub_model.pdf)
