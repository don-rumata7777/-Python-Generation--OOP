# "Поколение Python": ООП
# 4.8 Декоратор @singledispatchmethod

# Класс Negator

# Реализуйте класс Negator. При создании экземпляра класс не должен принимать никаких
# аргументов.

# Класс Negator должен иметь один статический метод:
# neg() — метод, принимающий в качестве аргумента объект и возвращающий его противоположное
# значение. Если методу передается целое или вещественное число, он должен возвращать это
# число, взятое с противоположным знаком. Если методу в качестве аргумента передается булево
# значение, он должен возвращать булево значение, противоположное переданному. Если переданный
# объект принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с
# текстом:
# Аргумент переданного типа не поддерживается

# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется,
# что реализованный класс используется только с корректными данными.

# Примечание 2. Никаких ограничений касательно реализации класса Negator нет, она может быть
# произвольной.

# Sample Input 1:

# print(Negator.neg(11.0))
# print(Negator.neg(-12))
# print(Negator.neg(True))
# print(Negator.neg(False))

# Sample Output 1:

# -11.0
# 12
# False
# True

# Sample Input 2:

# try:
#     Negator.neg('number')
# except TypeError as e:
#     print(e)

# Sample Output 2:

# Аргумент переданного типа не поддерживается
##############################################################################################

# Из-за использования аннотации типов в Python 3.10 - ошибка, в Python 3.12 работает
from functools import singledispatchmethod


class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @neg.register
    @staticmethod
    def _neg_int_float(data: int | float):
        return -data

    @neg.register
    @staticmethod
    def _neg_bool(data: bool):
        return not data
