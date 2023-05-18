import pickle


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'


p = Point(1, 2)
print(p)

with open('class_pickled', 'wb') as file:
    pickle.dump(p, file)

with open('class_pickled', 'rb') as file:
    loaded = pickle.load(file)

print(type(loaded))
print(loaded)
