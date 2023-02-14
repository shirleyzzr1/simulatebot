import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
class SENSOR:
    def __init__(self,linkName) -> None:
        self.linkName = linkName
        self.values = np.zeros(c.STEP)


    def Get_Value(self,t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        # print("values",self.values)

    def Save_Values(self):
        np.save("./data/"+self.values,self.values)
