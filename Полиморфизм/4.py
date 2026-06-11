class MinStat:
    def __init__(self):
        self._numbers = []

    def add_number(self, number):
        self._numbers.append(number)

    def result(self):
        if not self._numbers:
            return None
        return min(self._numbers)



class MaxStat:
    def __init__(self):
        self._numbers = []

    def add_number(self, number):
        self._numbers.append(number)

    def result(self):
        if not self._numbers:
            return None
        return max(self._numbers)



class AverageStat:
    def __init__(self):
        self._numbers = []

    def add_number(self, number):
        self._numbers.append(number)

    def result(self):
        if not self._numbers:
            return None
        return sum(self._numbers) / len(self._numbers)

