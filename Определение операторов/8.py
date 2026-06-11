class Queue:
    def __init__(self, *values):
        self._data = list(values)

    def append(self, *values):
        self._data.extend(values)

    def copy(self):
        return Queue(*self._data)

    def pop(self):
        if not self._data:
            return None
        return self._data.pop(0)

    def extend(self, queue):
        self._data.extend(queue._data)

    def next(self):
        if len(self._data) <= 1:
            return Queue()
        return Queue(*self._data[1:])

    def __add__(self, other):
        new_data = self._data + other._data
        return Queue(*new_data)

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __eq__(self, other):
        return self._data == other._data

    def __rshift__(self, n):
        if n >= len(self._data):
            return Queue()
        return Queue(*self._data[n:])

    def __str__(self):
        if not self._data:
            return '[]'
        return '[' + ' -> '.join(map(str, self._data)) + ']'

    def __next__(self):
        return self.next()


q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep='\n')
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)
