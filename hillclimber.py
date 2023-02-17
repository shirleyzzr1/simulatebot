from solution import SOLUTION
import constants as c
import copy
class HILL_CLIMBER:
    def __init__(self) -> None:
        self.parent = SOLUTION()
    
    def Evolve(self):
        self.parent.Evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()

        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        #parent is worse than child's fitness
        if self.parent.fitness>self.child.fitness:
            print("choose child fitness")
            self.parent = copy.deepcopy(self.child)
            # self.parent = self.child

    def Print(self):
        print("parent fitness: {}, child fitness: {}".format(self.parent.fitness,self.child.fitness))

    def Show_Best(self):
        self.parent.Evaluate("GUI")

