from random import randint
from pprint import pprint

n = int(input("N: "))
m = int(input("M: "))
a = int(input("A: "))
b = int(input("B: "))
arr = [[randint(a, b) for x in range(n)] for y in range(m)]

pprint(arr)