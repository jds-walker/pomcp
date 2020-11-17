from tiger import Tiger
from node import Node

tiger = Tiger()
tree = Node(tiger, actual_state=tiger.startState())


for i in range(10):
    # train 
    for _ in range(600):
        tree.select()

    # actual act
    print(i)
    tree = tree.act()


