from tiger import Tiger
from node import Node

tiger = Tiger()
tree = Node(tiger, actual_state=tiger.startState())

rewards = 0
for i in range(100):

    # train 
    for _ in range(1200):
        tree.select()

    # actual act
    tree, reward = tree.act()
    print(reward)
    rewards = rewards + reward


print(f"total rewarads {rewards}")