from tiger import Tiger
from node import Node

tiger = Tiger()
tree = Node(tiger)

for _ in range(600):
    tree.select()

tree.select()

print(tree.V)
print(tree.N)
