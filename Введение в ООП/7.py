class BoundingRectangle:
    def __init__(self):
        self._points = []
        self._min_x = None
        self._max_x = None
        self._min_y = None
        self._max_y = None

    def add_point(self, x, y):
        self._points.append((x, y))
        if self._min_x is None or x < self._min_x:
            self._min_x = x
        if self._max_x is None or x > self._max_x:
            self._max_x = x
        if self._min_y is None or y < self._min_y:
            self._min_y = y
        if self._max_y is None or y > self._max_y:
            self._max_y = y

    def width(self):
        return self._max_x - self._min_x

    def height(self):
        return self._max_y - self._min_y

    def bottom_y(self):
        return self._min_y

    def top_y(self):
        return self._max_y

    def left_x(self):
        return self._min_x

    def right_x(self):
        return self._max_x


rect = BoundingRectangle()
rect.add_point(-1, -2)
rect.add_point(3, 4)
print(rect.left_x(), rect.right_x())  
print(rect.bottom_y(), rect.top_y())  
print(rect.width(), rect.height())    
