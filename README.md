# mybots Simulation Project

## Overview

**mybots** is a robotics simulation environment built as part of an assignment submission for the [Ludobots Online Course](https://www.reddit.com/r/ludobots/wiki/installation/).  

The project explores how virtual systems can evolve, move, and adapt inside a simulated world using the **PyBullet** physics engine.  

Through incremental modules, learners build from simple one-link robots to complex, multi-jointed, sensor-driven agents capable of learning and adaptation.

---

## Project Goals

- Understand 3D physics-based simulation of robots.  
- Explore links, joints, sensors, and motors for controlled locomotion.  
- Implement simple neural controllers and evolutionary algorithms.  
- Gradually evolve robot behaviors using search strategies like **Random Search** and **Hill Climbing**.  
- Extend to parallelized learning and more complex designs (e.g., quadrupeds).  

---

## Branch Structure

Each branch corresponds to a specific milestone in the **Ludobots** curriculum.  
You can check out each branch to explore that module’s code and assignments.

| Branch | Description |
|:--|:--|
| **simulation** | Basic simulation setup using PyBullet and Pyrosim. |
| **onelink** | Introduction to creating a single-link robot and world. |
| **manylinks** | Multi-link body construction and hierarchical structures. |
| **joints** | Adding and controlling revolute joints between body parts. |
| **sensors** | Attaching and reading sensor values (touch, position, etc.). |
| **motors** | Controlling motion using motor commands and torque. |
| **refactoring** | Code cleanup and modularization for maintainability. |
| **neurons** | Implementing neuron-based controllers for behavior control. |
| **synapses** | Connecting neurons via weighted synapses for decision-making. |
| **randomsearch** | Exploring random parameter search for robot optimization. |
| **hillclimber** | Implementing the Hill Climber algorithm for local search optimization. |
| **parallelHC** | Parallelized version of Hill Climber for faster convergence. |
| **quadruped** | Designing and evolving a four-legged robot with realistic gait control. |
| **finalProject** | Integrating all modules into a full evolutionary robotics simulation. |

---

## Installation & Setup

Follow the setup guide on the official [Ludobots Wiki](https://www.reddit.com/r/ludobots/wiki/installation/) to install:

- **PyBullet**  
- **Pyrosim**  
- **NumPy**, 
- **Matplotlib**

Once installed, clone this repository and switch between branches to explore each stage:

```bash
git clone https://github.com/yourusername/MyBots.git
cd mybots
git checkout simulation 
python3 simulate.py
```
