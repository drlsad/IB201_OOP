class SparseArray:
    def __init__(self):
        self._data = {}

    def __setitem__(self, index, value):
        if value != 0:
            self._data[index] = value
        elif index in self._data:
            del self._data[index]

    def __getitem__(self, index):
        return self._data.get(index, 0)

arr = SparseArray()
arr[1] = 10
arr[8] = 20
for i in range(10):
    print('arr[{}] = {}'.format(i, arr[i]))
