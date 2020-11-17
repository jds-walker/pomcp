import unittest
from node import Node
from tiger import Tiger

class pomcpTests(unittest.TestCase):
    

    def test_UCT(self):

        t = Tiger()
        a = Node(t)

        a.N = 10

        a.children["b"] = Node(t)

        b = a.children["b"]

        b.N = 20

        

        self.fail("finish the test")





if __name__ == "__main__":
    unittest.main()
