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

    def delete_row(self, row):
        if 0 <= row < self._rows:
            del self._data[row]
            self._rows -= 1

    def delete_col(self, col):
        if 0 <= col < self._cols:
            for row in self._data:
                del row[col]
            self._cols -= 1

    def add_row(self, row):
        new_row = [0] * self._cols
        self._data.insert(row, new_row)
        self._rows += 1

    def add_col(self, col):
        