from world import WORLD
from robot import ROBOT
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import constants as c
import time
import numpy as np
class SIMULATION:
    def __init__(self) -> None:
        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        self.world = WORLD()
        self.robot = ROBOT()
        #p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        p.setGravity(0,0,c.Gravity)
        # pyrosim.Prepare_To_Simulate(self.robot.robotId)


    def run(self):
        for i in range(c.STEP):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)
            time.sleep(c.SLEEP)

    def __del__(self):
        p.disconnect()
