import numpy as np

import pybullet as p
import constants as c
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName, steps):
        self.jointName = jointName
        self.steps = steps

    def Set_Value(self, desiredAngle, robotId):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = c.MAX_FORCE)
    