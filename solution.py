import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
class SOLUTION:
    def __init__(self) -> None:
        self.weights = 2*np.random.rand(3,2)-1

    def Evaluate(self,directOrGUI):
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py "+directOrGUI)
        fitnessFile = open("fitness.txt", "r")
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()

    def Create_Body(self):
        pyrosim.Start_SDF("world.sdf")
        length,width,height = 1,1,1
        x,y,z = 2,2,0.5
        pyrosim.Send_Cube(name="Box",pos=[x,y,z],size=[length,width,height])
        pyrosim.End()

        pyrosim.Start_URDF("body.urdf")
        length,width,height = 1,1,1
        x,y,z = 0,0,0.5
        pyrosim.Send_Cube(name="Torso",pos=[1.5,0,1.5],size=[length,width,height])
        pyrosim.Send_Joint(name="Torso_BackLeg",parent = "Torso",child = "BackLeg",type="revolute",position = [1.0,0,1.0])
        pyrosim.Send_Cube(name="BackLeg",pos=[-0.5,0,-0.5],size=[length,width,height])
        pyrosim.Send_Joint(name="Torso_FrontLeg",parent = "Torso",child = "FrontLeg",type ="revolute",position = [2.0,0,1.0])
        pyrosim.Send_Cube(name="FrontLeg",pos=[0.5,0,-0.5],size=[length,width,height])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_SDF("world.sdf")
        length,width,height = 1,1,1
        x,y,z = 2,2,0.5
        pyrosim.Send_Cube(name="Box",pos=[x,y,z],size=[length,width,height])
        pyrosim.End()

        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron(name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 4 , jointName = "Torso_FrontLeg")

        #outer loop iterate over sensor neurons
        for currentRow in range(3):
            #inner loop iterate over sensor neurons
            for currentColumn in range(0,2):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+3 , weight = self.weights[currentRow][currentColumn] )

        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0,2)
        randomColumn = random.randint(0,1)
        self.weights[randomRow,randomColumn] = random.random()*2-1
        

