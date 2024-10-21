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
