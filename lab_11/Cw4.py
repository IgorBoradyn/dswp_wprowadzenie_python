import pickle


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'


p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = Point(5, 6)
p4 = Point(7, 8)
print(p1)
print(p2)
print(p3)
print(p4)

points = [p1, p2, p3, p4]

with open('classes_pickled', 'wb') as file:
    pickle.dump(points, file)

with open('classes_pickled', 'rb') as file:
    loaded = pickle.load(file)

print(type(loaded))
print(*loaded)
