# Zad 1
class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    # Zad 2
    def __str__(self):
        return f'Point({self.x}, {self.y})'

    # Zad 3
    def __mul__(self, other):
        self.x = self.x * other
        self.y = self.y * other

        return self

    # Zad 4
    def __eq__(self, other):
        return True if type(other) is Point and other.x == self.x and other.y == self.y else False


# Zad 2
p1 = Point()
print(p1)
p1.x = 2
p1.y = 5
print(p1)
# Zad 3
print(p1*2)

# Zad 4
p2 = Point(2, 5)
print(p2)
print(p1 == p2)
p2.x = p1.x
p2.y = p1.y
print(p1 == p2)


# Zad 5
class Polygon:
    def __init__(self):
        self.points = []

    def add_point(self, point: Point):
        self.points.append(point)

    # Zad 6
    def __str__(self):
        return f'Polygon[{", ".join(map(str, self.points))}]'

    # Zad 7
    def __getitem__(self, item):
        if isinstance(item, int):
            return self.points[item]
        elif isinstance(item, slice):
            return self.points[item.start:item.stop:item.step]
        else:
            raise TypeError("Item must be an integer or a slice object.")


# Zad 5
pol = Polygon()
pol.add_point(Point())
pol.add_point(Point(1, 1))
pol.add_point(Point(1, 2))
pol.add_point(Point(2, 1))
pol.add_point(Point(2, 2))

# Zad 6
print(pol)
# Zad 7
print(pol[0])
print(pol[4])
lst = pol[1:3]
print(lst)
print(lst[0])
print(lst[1])
