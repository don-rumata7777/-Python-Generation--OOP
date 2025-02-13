# "Поколение Python": ООП
# 5.3 Сравнение объектов

# Класс Month

# Реализуйте класс Month, описывающий месяц. При создании экземпляра класс должен
# принимать два аргумента в следующем порядке:
# year — год
# month — порядковый номер месяца

# Экземпляр класса Month должен иметь следующее формальное строковое представление:
# Month(<год>, <порядковый номер месяца>)

# И следующее неформальное строковое представление:
# <год>-<порядковый номер месяца>

# Также экземпляры класса Month должны поддерживать все операции сравнения с
# помощью операторов ==, !=, >, <, >=, <=. Два Month объекта считаются равными,
# если их годы и порядковые номера месяцев совпадают. Month объект считается
# больше другого Month объекта, если его год больше. В случае если два Month
# объекта имеют равные года, большим считается тот, чей месяц больше. Методы,
# реализующие операции сравнения, должны уметь сравнивать как два Month объекта
# между собой, так и Month объект с кортежем из двух чисел, представляющих год
# и месяц.

# Примечание 1. Если объект, с которым выполняется операция сравнения,
# некорректен, метод, реализующий эту операцию, должен вернуть константу
# NotImplemented.

# Примечание 2. Никаких ограничений касательно реализации класса Month нет,
# она может быть произвольной.


# Sample Input 1:

# print(Month(1999, 12) == Month(1999, 12))
# print(Month(1999, 12) < Month(2000, 1))
# print(Month(1999, 12) > Month(2000, 1))
# print(Month(1999, 12) <= Month(1999, 12))
# print(Month(1999, 12) >= Month(2000, 1))

# Sample Output 1:

# True
# True
# False
# True
# False

# Sample Input 2:

# months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]

# print(sorted(months))

# Sample Output 2:

# [Month(1998, 12), Month(1999, 12), Month(2000, 1)]
# Sample Input 3:

# months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]

# print(min(months))
# print(max(months))

# Sample Output 3:

# 1998-12
# 2000-1

##############################################################################################

from functools import total_ordering


@total_ordering
class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def __str__(self):
        return f"{self.year}-{self.month}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.year}, {self.month})"

    def __eq__(self, other):
        if isinstance(other, Month):
            return self.year == other.year and self.month == other.month
        elif isinstance(other, tuple):
            return (self.year, self.month) == other
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Month):
            return (self.year, self.month) > (other.year, other.month)
        elif isinstance(other, tuple):
            return (self.year, self.month) > other
        return NotImplemented
