class Balance:
    def __init__(self):
        self._right_weight = 0
        self._left_weight = 0

    def add_right(self, weight):
        self._right_weight += weight

    def add_left(self, weight):
        self._left_weight += weight

    def result(self):
        if self._left_weight > self._right_weight:
            return 'L'
        elif self._right_weight > self._left_weight:
            return 'R'
        else:
            return '='

balance = Balance()
balance.add_right(10)
balance.add_left(9)
balance.add_left(2)
print(balance.result())  
