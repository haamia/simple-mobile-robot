# Simple Mobile Robot
This project presents a beginner-level mobile robot model developed using URDF and visualized in RViz2. The robot consists of a base link, differential drive wheels, a LiDAR sensor, and a camera module to demonstrate the fundamentals of robot modeling in ROS 2.

The purpose of this project is to provide a simple introduction to robot description, link and joint relationships, coordinate frames, and sensor integration. It serves as a starting point for learning URDF, TF transforms, RViz visualization, and mobile robot simulation workflows in ROS 2.

## Robot Model

<p align="center">
  <img src="images/robot_model.png" width="700">
</p>

## Structure

base_link
├── left_wheel
├── right_wheel
├── lidar_link
└── camera_link