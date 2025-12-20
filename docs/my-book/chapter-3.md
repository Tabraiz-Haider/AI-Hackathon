
<div id="language-selector">
  <label for="lang-select">Select Language: </label>
  <select id="lang-select" onchange="changeLanguage(this.value)">
    <option value="en">English</option>
    <option value="ur">Urdu</option>
    <option value="hi">Hindi</option>
    <option value="ar">Arabic</option>
  </select>
</div>

<!-- Translation functionality will be handled by Docusaurus theme components -->

# Chapter 3: Sensors & Actuators

## 3.1 Role of Sensors in Robotics

Sensors are the robot's eyes, ears, and touch, providing the crucial data necessary for perceiving its internal state and the external environment. Without accurate sensory information, a robot cannot navigate, interact with objects, or make intelligent decisions. Sensors convert physical phenomena into electrical signals that can be processed by the robot's control system, enabling feedback mechanisms and environmental awareness essential for autonomous operation.

## 3.2 Types of Sensors

Robots employ a wide array of sensors, each serving specific purposes:

*   **Proprioceptive Sensors:** Measure the robot's internal state.
    *   **Encoders:** Measure joint angles and motor rotation (position and velocity).
    *   **IMUs (Inertial Measurement Units):** Provide orientation, angular velocity, and linear acceleration using accelerometers and gyroscopes.
    *   **Force/Torque Sensors:** Measure forces and torques exerted at joints or end-effectors, crucial for compliant manipulation.
*   **Exteroceptive Sensors:** Measure information about the external environment.
    *   **Vision Sensors (Cameras):** Capture visual data for object recognition, tracking, and scene understanding.
    *   **Lidar (Light Detection and Ranging):** Uses pulsed laser light to measure distances to objects, creating detailed 3D maps of the environment.
    *   **Sonar (Sound Navigation and Ranging):** Uses sound waves to detect objects and measure distances, often used for obstacle avoidance.
    *   **Tactile Sensors:** Detect physical contact and pressure, enabling robots to "feel" objects.
    *   **Proximity Sensors:** Detect the presence of nearby objects without physical contact (e.g., infrared, ultrasonic).

## 3.3 Role of Actuators in Robotics

Actuators are the components responsible for converting control signals into physical motion. They are the muscles of the robot, enabling it to move its joints, grip objects, and exert forces on its environment. The choice of actuator significantly impacts a robot's speed, strength, precision, and energy consumption.

## 3.4 Types of Actuators

Common types of actuators used in robotics include:

*   **Electric Motors:**
    *   **DC Motors:** Simple, robust, and widely used for continuous rotation.
    *   **Stepper Motors:** Provide precise angular positioning without feedback, ideal for controlled steps.
    *   **Servo Motors:** Integrate a DC motor with a gearbox and a feedback control loop for precise position, velocity, and torque control.
*   **Hydraulic Actuators:** Use pressurized fluid to generate large forces, often found in heavy-duty industrial robots.
*   **Pneumatic Actuators:** Use compressed air to produce linear or rotary motion, commonly used for grippers and simple pick-and-place tasks.
*   **Smart Materials:** Emerging actuators like Shape Memory Alloys (SMAs) or Dielectric Elastomer Actuators (DEAs) offer novel possibilities for compact and compliant robotic designs.

The intelligent integration of sensors and actuators, coupled with sophisticated control algorithms, is fundamental to creating versatile and capable physical AI systems.