# "Поколение Python": ООП
# 4.8 Декоратор @singledispatchmethod

# Класс Processor

# Вам доступен класс Processor. При создании экземпляра класс не принимает никаких аргументов.

# Класс Processor имеет один статический метод:
# process() — метод, который принимает в качестве аргумента произвольный объект, преобразует 
# его в зависимости от его типа и возвращает полученный результат. Если тип переданного объекта 
# не поддерживается методом, возбуждается исключение TypeError с текстом:
# Аргумент переданного типа не поддерживается
# 
# Перепишите метод process() класса Processor с использованием декоратора 
# @singledispatchmethod, чтобы он выполнял ту же задачу.

# Примечание 1. Примеры преобразования объектов всех поддерживаемых типов показаны в методе 
# process() класса Processor.

# Примечание 2. Никаких ограничений касательно реализации класса Processor нет, она может 
# быть произвольной.

# Sample Input 1:

# print(Processor.process(10))
# print(Processor.process(5.2))
# print(Processor.process('hello'))
# print(Processor.process((4, 3, 2, 1)))
# print(Processor.process([3, 2, 1]))

# Sample Output 1:

# 20
# 10.4
# HELLO
# (1, 2, 3, 4)
# [1, 2, 3]

# Sample Input 2:

# try:
#     Processor.process({1, 2, 3})
# except TypeError as e:
#     print(e)

# Sample Output 2:

# Аргумент переданного типа не поддерживается

##############################################################################################

from functools import singledispatchmethod

class Processor:
    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @process.register(int)
    @process.register(float)
    @staticmethod
    def _from_int_float(data):
        return data * 2

    @process.register(str)
    @staticmethod
    def _from_str(data):
        return data.upper()

    @process.register(list)
    @staticmethod
    def _from_list(data):
        return sorted(data)

    @process.register(tuple)
    @staticmethod
    def _from_tuple(data):
        return tuple(sorted(data))
