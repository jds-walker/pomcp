from scenario import Scenario
from node import Node
import random
import logging
from datetime import datetime

def main():
    logging.basicConfig(filename="./logging/" + str(datetime.now()) + '.txt')

    seed = random.rand()
    logging.warning('seed', seed)
    random.seed(seed)

    scenario = Scenario('./scenario/es1_red_d.yaml')

    tree = Node(scenario, actual_state=scenario.startState(), particles=5000, gamma=.9, c=1000)


    rewards = 0
    while tree.actual_state['terminal'] == False:



        # train 
        for _ in range(2000):
            tree.select()

        # actual act
        # particle update is done as part of the real step. 
        # Get next belief (function) take current particles - get action and observation -> from there generate next set of particles
        tree, reward = tree.act()
        print(reward)
        rewards = rewards + reward


    # Get average over at least 100 runs (average - total discounted reward - 95% confidence interval)
    # Hyperparameters (c = 100, 200, ... , 1000)
    # keep logs of every state / action 
    # set random seed in one place that makes the scenario determinstic (e.g time(now)) - random until we want to check
    # Generate new belief state when no real observation in tree. 

    print(f"total rewarads {rewards}")

if __name__ ==  '__main__':
    main()
