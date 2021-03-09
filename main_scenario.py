from scenario import Scenario
from node import Node

scenario = Scenario('./scenario/es1_red_d.yaml')

tree = Node(scenario, actual_state=scenario.startState())

rewards = 0
while tree.actual_state['terminal'] == False:

    # train 
    for _ in range(600):
        tree.select()

    # actual act
    # particle update is done as part of the real step. 
    # Get next belief (function) take current particles - get action and observation -> from there generate next set of particles
    tree, reward = tree.act()
    print(reward)
    rewards = rewards + reward


print(f"total rewarads {rewards}")