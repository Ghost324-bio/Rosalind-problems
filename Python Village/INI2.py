#For calculating hypotenuse, we need import math module and make whole input with map()
from math import pow, sqrt

a, b = map(int, input().split())

c2 = pow(a, 2) + pow(b, 2)
c = sqrt(c2)

print(c2)
print(c)