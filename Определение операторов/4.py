class Date:
    _days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, month, day):
        self._month = month
        self._day = day

    def _to_days(self):
        """Преобразует дату в количество дней с начала года"""
        total_days = 0
        for m in range(1, self._month):
            total_days += self._days_in_month[m]
        total_days += self._day
        return total_days

    def __sub__(self, other):
        """Вычитание дат: возвращает разницу в днях"""
        days_self = self._to_days()
        days_other = other._to_days()
        return days_self - days_other



jan5 = Date(1, 5)
jan1 = Date(1, 1)

print(jan5 - jan1)  
print(jan1 - jan5)  
print(jan1 - jan1)  
print(jan5 - jan5)  
