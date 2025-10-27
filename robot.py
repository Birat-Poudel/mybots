import os

import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

import constants as c
from sensor import SENSOR
from motor import MOTOR


class ROBOT:

    def __init__(self, steps, solutionID):
        self.steps = steps
        self.myID = solutionID
        self.sensors = {}
        self.motors = {}
        self.nn = NEURAL_NETWORK("brain" + str(self.myID) + ".nndf")

        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        os.system("rm brain" + str(self.myID) + ".nndf")
        
    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName, self.steps)

    def Sense(self, t):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(t)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName, self.steps)
    
    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(desiredAngle * c.MOTOR_JOINT_RANGE, self.robotId)

    def Think(self):
        self.nn.Update()
        # self.nn.Print()
    
    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        f = open("tmp" + str(self.myID) + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.system("mv tmp" + str(self.myID) + ".txt fitness" + str(self.myID) + ".txt")
