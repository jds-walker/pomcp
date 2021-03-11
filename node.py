from simulator import Simulator
from random import choice
from math import sqrt, log


class  Node():
    
    def __init__(self, simulator: Simulator, actual_state = None, particles: int = 1200, T = 0, gamma = .75, c = 100):
        self.simulator = simulator
        self.actual_state = actual_state
        self.particles = [simulator.startState() for _ in range(particles)] # belief state
        self.N = 0 # number of visits
        self.V = 0 # average value of rewards
        self.T = T # timestep
        self.gamma = gamma # discount factor 
        self.c = c # exploration factor
        self.children = dict()

    def select(self):


        self.simulator.state = choice(self.particles)        
        self.V = self.simulate() + (self.V * self.N)/(self.N+1)
        self.N += 1


    def simulate(self):
        
        if len(self.children) == 0: # create action children
            for action in self.simulator.allActions():
                self.children[action] = Node(self.simulator, particles=0, T=self.T+1, gamma=self.gamma)

        smallestNkey = min(self.children, key=lambda n: self.children[n].N)
        smallestN = self.children[smallestNkey].N
        if smallestN == 0: # explore unexplored actions
            smallestkeys = [k for k,v in self.children.items() if v.V == smallestN]
            smallestNkey = choice(smallestkeys)
            s, o, r = self.simulator.generate(self.simulator.state, smallestNkey)

            self.children[smallestNkey].children[o] = Node(self.simulator, particles=0, T=self.T+1, gamma=self.gamma)
            
            rollout_reward = self.children[smallestNkey].children[o].rollout()       

            self.children[smallestNkey].N = 1
            self.children[smallestNkey].V = r * (self.gamma ** (self.T)) + rollout_reward
            

            self.children[smallestNkey].children[o].N = 1
            self.children[smallestNkey].children[o].V = r * (self.gamma ** (self.T)) + rollout_reward
            self.children[smallestNkey].children[o].particles.append(s)
            
            return self.children[smallestNkey].children[o].V
        
        else:
          
            maxV = max(self.children, key=lambda n: self.children[n].V + self.c * sqrt(log(self.N)/self.children[n].N))

            s, o, r = self.simulator.generate(self.simulator.state, maxV)

            self.simulator.state = s

            if o not in self.children[maxV].children: 
                 self.children[maxV].children[o] = Node(self.simulator, particles=0, T=self.T+1, gamma=self.gamma)
                

            self.children[maxV].children[o].particles.append(s)

            reward = self.children[maxV].children[o].simulate()

            self.children[maxV].V = (reward + r * (self.gamma ** self.T+1) + (self.children[maxV].V * self.children[maxV].N)) / (self.children[maxV].N + 1)
            self.children[maxV].N += 1

            self.children[maxV].children[o].N += 1

            return reward

    def rollout(self, steps = 10):

        rewards = 0
        for i in range(steps):
            discount = self.gamma ** (self.T + i)
            state, _, reward = self.simulator.generate(self.simulator.state,choice(self.simulator.allActions()))
            self.simulator.state = state
            rewards += (reward * discount)

        return rewards

    def act(self):

        new_tree = None
        maxV = max(self.children, key=lambda n: self.children[n].V)
        print(maxV)
        real_state, real_observation, real_reward = self.simulator.generate(self.actual_state, maxV)

        if real_observation in self.children[maxV].children.keys():
            new_tree = self.children[maxV].children[real_observation]
            new_tree.actual_state = real_state

        else: 
            new_tree = Node(self.simulator, actual_state=real_state, particles=0, T=self.T, gamma=self.gamma,c=self.c)
            self.children[real_observation] = new_tree

        while len(new_tree.particles) < 1000:
            rand_state = choice(self.particles)
            state, observation, reward = self.simulator.generate(rand_state, maxV)
            if observation == real_observation:
                new_tree.particles.append(state) 

        return (self.children[maxV].children[real_observation], real_reward)
                
