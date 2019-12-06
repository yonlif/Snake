class Point:
    def __init__(self, x=0, y=0, size=5):
        self.x = x
        self.y = y
        self.size = size

    def __eq__(self, other):
        if other is None:
            return False
        return other.x == self.x and other.y == self.y

    def shape(self):
        return self.x * self.size, self.y * self.size, self.size, self.size

    def __copy__(self):
        return Point(self.x, self.y, self.size)
