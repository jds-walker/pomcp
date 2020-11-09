from simulator import Simulator
from random import choice


class  Node():
    
    def __init__(self, simulator: Simulator, particles: int = 1200):
        self.simulator = simulator
        self.particles = [simulator.startState() for _ in range(particles)]
        self.N = 0
        self.V = 0
        self.children = dict()

    def select(self):
        if len(self.children) == 0:
            # create action children, first observation & rollout
            for action in self.simulator.allActions():
                self.children[action] = Node(self.simulator, particles=0)
            action = choice(self.simulator.allActions())
            update = self.simulator.generate(self.simulator.state, action)
            # self.children[action].children[update[1]] = Node(self.simulator, particles=0)
            # self.children[action].children[update[1]].rollout()
            

        state, observation, reward = self.simulator.generate(choice(self.particles), choice(self.simulator.allActions()))
        print(state, observation, reward)

    def rollout(self, steps = 100):
        for _ in range(steps):
            s, o, r = self.simulator.generate(self.simulator.state,choice(self.simulator.allActions()))

