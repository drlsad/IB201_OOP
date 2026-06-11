class Rectangle:
    def __init__(self, x, y, w, h):
        self._x = x
        self._y = y
        self._w = w
        self._h = h

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_w(self):
        return self._w

    def get_h(self):
        return self._h

    def intersection(self, other):
        x1 = max(self._x, other._x)
        y1 = max(self._y, other._y)
        x2 = min(self._x + self._w, other._x + other._w)
        y2 = min(self._y + self._h, other._y + other._h)
        if x1 < x2 and y1 < y2:
            w = x2 - x1
            h = y2 - y1
            return Rectangle(x1, y1, w, h)
        else:
            return None


rect1 = Rectangle(0, 0, 10, 10)
rect2 = Rectangle(5, 5, 10, 10)
rect3 = rect1.intersection(rect2)

if rect3 is None:
    print('No intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())
