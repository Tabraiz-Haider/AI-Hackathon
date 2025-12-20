# Chapter 2: Robotics Fundamentals

## 2.1 Definition and History of Robotics

Robotics is an interdisciplinary field that integrates computer science, engineering, and artificial intelligence to design, construct, operate, and apply robots. The term "robot" was coined by Karel Čapek in his 1920 play *R.U.R.* (Rossum's Universal Robots). Early developments in robotics, particularly in the mid-20th century, focused on industrial automation with manipulators designed for repetitive tasks in controlled environments. Pioneers like George Devol and Joseph Engelberger established the foundations for modern industrial robotics, leading to widespread adoption in manufacturing.

## 2.2 Types of Robots

Robots come in various forms, each suited for different applications:

*   **Industrial Robots:** Stationary manipulators used in factories for tasks such as welding, painting, assembly, and material handling. Examples include articulated robots, SCARA robots, and gantry robots.
*   **Mobile Robots:** Robots capable of locomotion, often equipped with wheels, tracks, or legs, used for navigation, exploration, and delivery in diverse environments. Examples include autonomous guided vehicles (AGVs), drones, and planetary rovers.
*   **Humanoid Robots:** Robots designed to resemble the human body, possessing capabilities for bipedal locomotion, manipulation, and human-like interaction. Their form factor makes them suitable for operating in environments designed for humans.
*   **Medical Robots:** Used in healthcare for surgical assistance, rehabilitation, drug delivery, and patient monitoring.
*   **Service Robots:** Robots deployed in service industries, ranging from domestic cleaning robots to professional robots in hospitality and retail.

## 2.3 Robot Anatomy and Components

A typical robot consists of several fundamental components:

*   **Manipulator/Mechanism:** The physical structure that allows the robot to perform tasks, often composed of links and joints (e.g., robotic arm).
*   **End-Effector:** The tool attached to the end of the manipulator that interacts with the environment (e.g., grippers, welding torches, surgical instruments).
*   **Power Supply:** Provides energy to the robot's motors and electronics (e.g., batteries, hydraulic systems, pneumatic systems).
*   **Sensors:** Used to gather information about the robot's internal state and external environment (e.g., position sensors, force sensors, cameras).
*   **Controller:** The "brain" of the robot, responsible for processing sensor data, executing motion commands, and coordinating actions. This often includes a combination of hardware and software.

## 2.4 Degrees of Freedom (DOF)

Degrees of Freedom (DOF) define the number of independent parameters that specify the configuration of a robotic system. Each joint in a robot's arm typically contributes one or more DOFs, allowing for translational or rotational motion. A higher number of DOFs generally allows for greater dexterity and flexibility in task execution but also increases complexity in control. Understanding DOFs is crucial for analyzing a robot's workspace, reach, and maneuverability.