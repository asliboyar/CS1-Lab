#4.check the given positive integer is perfect square.
import math
a = int(input())
root =math.sqrt(a)
if int(root) ** 2 == a:
    print("True")
else:
    print("False")
