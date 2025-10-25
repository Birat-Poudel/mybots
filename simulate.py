import os
import time

import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim


physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8,physicsClient)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(1/120)

save_path = os.path.join(os.path.dirname(__file__), "data", "back_leg_sensor_values.npy")
np.save(save_path, backLegSensorValues)

save_path = os.path.join(os.path.dirname(__file__), "data", "front_leg_sensor_values.npy")
np.save(save_path, frontLegSensorValues)

p.disconnect()
