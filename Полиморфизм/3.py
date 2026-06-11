class AmericanDate:
    def __init__(self, year, month, day):
        self._year = year
        self._month = month
        self._day = day

    def set_year(self, year):
        self._year = year

    def set_month(self, month):
        self._month = month

    def set_day(self, day):
        self._day = day

    def get_year(self):
        return self._year

    def get_month(self):
        return self._month

    def get_day(self):
        return self._day

    def format(self):
        return f"{self._month:02d}.{self._day:02d}.{self._year:04d}"



class EuropeanDate:
    def __init__(self, year, month, day):
        self._year = year
        self._month = month
        self._day = day

    def set_year(self, year):
        self._year = year

    def set_month(self, month):
        self._month = month

    def set_day(self, day):
        self._day = day

    def get_year(self):
        return self._year

    def get_month(self):
        return self._month

    def get_day(self):
        return self._day

    def format(self):
        return f"{self._day:02d}.{self._month:02d}.{self._year:04d}"

