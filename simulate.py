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

BackLegAmplitude = np.pi/6
BackLegFrequency = 2.0
BackLegPhaseOffset = 0

FrontLegAmplitude = np.pi/6
FrontLegFrequency = 2.0
FrontLegPhaseOffset = 2 * np.pi + 0.1

BackLegTargetAngles = np.zeros(1000)
FrontLegTargetAngles = np.zeros(1000)

for i in range(1000):
    BackLegTargetAngles[i] = BackLegAmplitude * np.sin(BackLegFrequency * i * np.pi/60 + BackLegPhaseOffset)
    FrontLegTargetAngles[i] = FrontLegAmplitude * np.sin(FrontLegFrequency * i * np.pi/60 + FrontLegPhaseOffset)

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = BackLegTargetAngles[i],
        maxForce = 500)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = FrontLegTargetAngles[i],
        maxForce = 500)
    time.sleep(1/240)

save_path = os.path.join(os.path.dirname(__file__), "data", "back_leg_sensor_values.npy")
np.save(save_path, backLegSensorValues)

save_path = os.path.join(os.path.dirname(__file__), "data", "front_leg_sensor_values.npy")
np.save(save_path, frontLegSensorValues)

p.disconnect()
