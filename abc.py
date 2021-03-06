from enum import Enum

class A(Enum):
    B = [True, False]
    C = [True, False]

print(A.C.value)