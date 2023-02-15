import pyrosim.pyrosim as pyrosim
def Create_World():
    pyrosim.Start_SDF("world.sdf")
    length,width,height = 1,1,1
    x,y,z = 2,2,0.5
    pyrosim.Send_Cube(name="Box",pos=[x,y,z],size=[length,width,height])
    pyrosim.End()
def Generate_Body():
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

def Generate_Brain():
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

    pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = 1.0 )
    pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 1.0 )

    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    length,width,height = 1,1,1
    x,y,z = 0,0,0.5
    pyrosim.Send_Cube(name="Torso",pos=[1.5,0,1.5],size=[length,width,height])
    pyrosim.Send_Joint(name="Torso_BackLeg",parent = "Torso",child = "BackLeg",type="revolute",position = [1.0,0,1.0])
    pyrosim.Send_Cube(name="BackLeg",pos=[-0.5,0,-0.5],size=[length,width,height])
    pyrosim.Send_Joint(name="Torso_FrontLeg",parent = "Torso",child = "FrontLeg",type ="revolute",position = [2.0,0,1.0])
    pyrosim.Send_Cube(name="FrontLeg",pos=[0.5,0,-0.5],size=[length,width,height])
    pyrosim.End()

# Create_World()
# Create_Robot()
Generate_Body()
Generate_Brain()
