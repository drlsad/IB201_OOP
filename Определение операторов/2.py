class ReversedList:
    def __init__(self, lst):
        self._data = lst[::-1]  

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]


rl = ReversedList([10, 20, 30])
for i in range(len(rl)):
    print(rl[i])


