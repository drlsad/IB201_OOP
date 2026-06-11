import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @classmethod
    def from_string(cls, s: str) -> "Point":
        x_str, y_str = s.replace(" ", "").split(",")
        return cls(float(x_str), float(y_str))

    @classmethod
    def from_dict(cls, d: dict) -> "Point":
        return cls(d["x"], d["y"])


    @staticmethod
    def distance(a: "Point", b: "Point") -> float:
        dist = math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
        return round(dist, 2)

p1 = Point.from_string("3, 4")
p2 = Point.from_dict({"x": 0, "y": 0})
print(p1.x, p1.y)  
print(Point.distance(p1, p2))  

