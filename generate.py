import pyrosim.pyrosim as pyrosim
def Create_World():
    pyrosim.Start_SDF("world.sdf")
    length,width,height = 1,1,1
    x,y,z = 2,2,0.5
    pyrosim.Send_Cube(name="Box",pos=[x,y,z],size=[length,width,height])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    length,width,height = 1,1,1
    x,y,z = 0,0,0.5
    pyrosim.Send_Cube(name="Torso",pos=[0,0,0.5],size=[length,width,height])
    pyrosim.Send_Joint(name="Torso_BackLeg",parent = "Torso",child = "BackLeg",type="revolute",position = [0,0.5,1.0])
    pyrosim.Send_Cube(name="BackLeg",pos=[0,0.5,0.5],size=[length,width,height])
    pyrosim.Send_Joint(name="BackLeg_FrontLeg",parent = "BackLeg",child = "FrontLeg",type ="revolute",position = [0,1.0,0])
    pyrosim.Send_Cube(name="FrontLeg",pos=[0,0.5,-0.5],size=[length,width,height])
    pyrosim.End()

Create_World()
Create_Robot()
