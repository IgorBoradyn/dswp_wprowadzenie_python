from timeit import timeit

setup = """
from collections import deque
import random
import string

d = deque()
l = list()
n = 100_000
"""

stmt1_1 = """
for i in range(n):
    d.append(i)
"""
stmt1_2 = """
for i in range(n):
    d.appendleft(i)
"""

stmt2_1 = """
for i in range(n):
    l.append(i)
"""
stmt2_2 = """
for i in range(n):
    l.insert(0, i)
"""

print(timeit(stmt1_1, setup, number=100))
print(timeit(stmt1_2, setup, number=100))
print(timeit(stmt2_1, setup, number=100))
print(timeit(stmt2_2, setup, number=1))
