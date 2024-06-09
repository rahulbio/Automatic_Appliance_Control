# Automatic_Appliance_Control
## Overview

This project addresses the critical need for energy conservation by optimizing the usage of electrical appliances. Leveraging computer vision and IoT, we enable real-time monitoring and control of energy consumption in various environments such as classrooms, labs, and industries. The proposed system uses existing CCTV cameras, minimizing additional hardware requirements, and implements smart algorithms to achieve substantial energy savings and cost reduction.

## Features

- **Real-Time Monitoring**: Utilizes YOLOv5 for real-time person detection.
- **Energy Management**: Automatically controls electrical devices based on human activity.
- **IoT Integration**: Employs a client-server architecture with Raspberry Pi for device control.
- **Minimal Hardware**: Easily implemented using existing CCTV cameras.

- ## Aim

The aim of this project is to implement a computer vision-based approach using the YOLOv5 model for real-time detection of persons in a specific region. The system controls electrical devices in a room to conserve energy when they are not in use. A client-server architecture is proposed where the server (model) provides information to the client (Raspberry Pi), which then controls devices like lights and fans based on the detected human activity.

## System Architecture

The system follows a client-server architecture:
- **Server**: Runs the YOLOv5 model for real-time person detection and sends the information to the client.
- **Client (Raspberry Pi)**: Receives data from the server and controls electrical devices based on the detected human activity.

## Usage

1. Set up your CCTV cameras for capturing the environment.
2. Run the server to start the YOLOv5 model for person detection:
   python server.py

3. Configure the Raspberry Pi as the client to receive data from the server and control devices by accessing the client.ipynb file
4. Monitor and control energy consumption based on real-time person detection.

## Results

The implementation of this system has shown a substantial reduction in energy consumption by automatically turning off unused electrical appliances. This leads to significant cost savings and a positive environmental impact.

