import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p
class MOTOR:
    def __init__(self,jointName) -> None:
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.Bamplitude
        if self.jointName ==b'Torso_BackLeg':
            self.frequency = c.Bfrequency/2
        else:
            self.frequency = c.Bfrequency
        self.offset = c.BphaseOffset
        x = np.linspace(0,2*np.pi,c.STEP)
        self.motorValues = [self.amplitude*np.sin(self.frequency*x[i]+self.offset) for i in range(len(x))]

    def Set_Value(self,robotId,t):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[t],
            maxForce = c.maxForce)

    def Save_Values(self):
        np.save("./data/"+self.motorValues,self.motorValues)


