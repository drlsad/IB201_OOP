class Table:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
      
        self._data = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        if 0 <= row < self._rows and 0 <= col < self._cols:
            return self._data[row][col]
        else:
            return None

    def set_value(self, row, col, value):
    
        self._data[row][col] = value

    def n_rows(self):
        return self._rows

    def n_cols(self):
        return self._cols
tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()


