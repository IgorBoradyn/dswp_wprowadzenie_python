from timeit import timeit

setup = """
from array import array
import random
import string
"""

stmt1_1 = """
tab_of_ints = array('i', [random.randint(-1_000, 1_000) for _ in range(100_000)])
"""
stmt1_2 = """
tab_of_longs = array('l', [random.randint(-1_000_000_000, 1_000_000_000) for _ in range(100_000)])
"""
stmt1_3 = """
tab_of_strs = array('u', [random.choice(string.ascii_letters) for _ in range(100_000)])
"""

stmt2_1 = """
list_of_ints = [random.randint(-1_000, 1_000) for _ in range(100_000)]
"""
stmt2_2 = """
list_of_longs = [random.randint(-1_000_000_000, 1_000_000_000) for _ in range(100_000)]
"""
stmt2_3 = """
list_of_strs = [random.choice(string.ascii_letters) for _ in range(100_000)]
"""

print(timeit(stmt1_1, setup, number=100))
print(timeit(stmt1_2, setup, number=100))
print(timeit(stmt1_3, setup, number=100))
print(timeit(stmt2_1, setup, number=100))
print(timeit(stmt2_2, setup, number=100))
print(timeit(stmt2_3, setup, number=100))
