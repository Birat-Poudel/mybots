import numpy as np

import pybullet as p
import constants as c
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName, steps):
        self.jointName = jointName
        self.steps = steps

        self.Prepare_To_Act()
    
    def Prepare_To_Act(self):
        self.motorValues = np.linspace(-np.pi, np.pi, self.steps)
        self.amplitude = c.AMPLITUDE
        self.frequency = c.FREQUENCY
        self.offset = c.OFFSET

        if self.jointName == b'Torso_BackLeg':
            self.frequency *= 0.5

        for i in range(self.steps):
            self.motorValues[i]= self.amplitude * np.sin(self.frequency * self.motorValues[i] + self.offset)
    
    def Set_Value(self, t, robotId):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[t],
            maxForce = c.MAX_FORCE)
    
    def Save_Values(self):
        np.save('data/' + self.jointName + 'MotorValues.npy', self.motorValues)
