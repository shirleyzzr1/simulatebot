import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c
from simulation import SIMULATION
import sys
directOrGUI = sys.argv[1]
simulation = SIMULATION(directOrGUI)
simulation.run()
simulation.Get_Fitness()

