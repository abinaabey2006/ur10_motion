# UR10 3-Point Motion Controller

<p align="center">
  <img src="https://img.shields.io/badge/ROS2-Humble-blue?style=flat-square&logo=ros" />
  <img src="https://img.shields.io/badge/Ubuntu-22.04-orange?style=flat-square&logo=ubuntu" />
  <img src="https://img.shields.io/badge/Gazebo-Simulation-green?style=flat-square" />
  <img src="https://img.shields.io/badge/MoveIt-2-red?style=flat-square" />
  <img src="https://img.shields.io/badge/Python-3.10-yellow?style=flat-square&logo=python" />
</p>

A lightweight ROS2 Humble package that commands a **Universal Robots UR10** manipulator through an automated 3-position joint trajectory sequence. Built for Gazebo simulation with MoveIt/RViz integration.

---

## Demo

The robot executes a continuous cycle:
- **Position 1** → Home / Up
- **Position 2** → Right Side Reach
- **Position 3** → Left Side Reach

---

## Features

- **Direct Trajectory Publishing** — Publishes `JointTrajectory` messages directly to the controller
- **Automated Sequence** — Hands-free execution through 3 predefined joint configurations
- **Simulation-Ready** — Compatible with Gazebo, RViz, and MoveIt out of the box
- **Minimal & Extensible** — Pure Python, no unnecessary dependencies

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Middleware | ROS2 Humble Hawksbill |
| OS | Ubuntu 22.04 LTS |
| Simulator | Gazebo Ignition / Classic |
| Motion Planning | MoveIt 2 |
| Robot | Universal Robots UR10 |
| Language | Python 3 |

---

## Prerequisites

Ensure your workspace has the UR simulation packages:

```bash
# In your ur_ws
ros2 launch ur_simulation_gazebo ur_sim_moveit.launch.py ur_type:=ur10

Quick Start
1. Clone & Build
bash
Copy

cd ~/ur_ws/src
git clone https://github.com/abinaabey2006/ur10_motion.git
cd ~/ur_ws
colcon build --packages-select ur10_motion --symlink-install
source install/setup.bash

2. Launch the Simulation
bash
Copy

# Terminal 1
ros2 launch ur_simulation_gazebo ur_sim_moveit.launch.py ur_type:=ur10

Wait until Gazebo and RViz fully load.
3. Run the Motion Node
bash
Copy

# Terminal 2
ros2 run ur10_motion ur10_3point

You will see the UR10 move through all 3 positions automatically.
Configuration
Controller Topic
If your setup uses a different controller, update the topic in ur10_3point_node.py:
Python
Copy

# Current setup
'/joint_trajectory_controller/joint_trajectory'

# Alternative setups
# '/scaled_joint_trajectory_controller/joint_trajectory'

Target Positions
Modify the self.positions array (all values in radians):
Python
Copy

[0.0, -1.57, 1.57, 0.0, 0.0, 0.0],   # Home
[1.0, -1.0, 1.0, -0.5, 0.5, 0.0],    # Right
[-1.0, -1.2, 0.8, 0.5, -0.5, 0.0]    # Left

Order: [shoulder_pan, shoulder_lift, elbow, wrist_1, wrist_2, wrist_3]
Project Structure
plain
Copy

ur10_motion/
├── ur10_motion/
│   ├── __init__.py
│   └── ur10_3point_node.py       # Main trajectory publisher
├── resource/
│   └── ur10_motion
├── package.xml
├── setup.py
├── setup.cfg
└── README.md

Roadmap

    [ ] Trigger motion via ROS2 Service instead of auto-start
    [ ] Add Cartesian path planning via MoveIt Python API
    [ ] Integrate collision avoidance
    [ ] Deploy on physical UR10 hardware


Author
Abina Abey
