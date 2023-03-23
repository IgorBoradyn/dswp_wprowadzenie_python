import random

A = [[random.randint(0, 50) for _ in range(4)] for _ in range(4)]

for x in A:
    print(x)
print()

B = [A[x][x] for x in range(4)]

print(B)
