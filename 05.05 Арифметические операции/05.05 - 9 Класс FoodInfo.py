# "Поколение Python": ООП
# 5.5 Арифметические операции


# Класс FoodInfo

# Реализуйте класс FoodInfo, описывающий пищевую ценность продуктов. При создании 
# экземпляра класс должен принимать три аргумента в следующем порядке:
# proteins — количество белков в граммах
# fats — количество жиров в граммах
# carbohydrates — количество углеводов в граммах

# Экземпляр класса FoodInfo должен иметь три атрибута:
# proteins — количество белков в граммах
# fats — количество жиров в граммах
# carbohydrates — количество углеводов в граммах

# И следующее формальное строковое представление:
# FoodInfo(<количество белков>, <количество жиров>, <количество углеводов>)

# Также экземпляры класса FoodInfo должны поддерживать между собой операцию сложения 
# с помощью оператора +, результатом которой должен являться новый экземпляр класса 
# FoodInfo с суммарным количеством белков, жиров и углеводов исходных экземпляров.

# Наконец, экземпляр класса FoodInfo должен поддерживать операции умножения, деления 
# и деления нацело на число n с помощью операторов *, / и // соответственно:

# результатом умножения должен являться новый экземпляр класса FoodInfo, количество 
# белков, жиров и углеводов которого умножены на n
# результатом деления должен являться новый экземпляр класса FoodInfo, количество 
# белков, жиров и углеводов которого поделены на n
# результатом деления нацело должен являться новый экземпляр класса FoodInfo, 
# количество белков, жиров и углеводов которого поделены нацело на n

# Примечание 1. Числами будем считать экземпляры классов int и float. Также будем 
# гарантировать, что экземпляр класса FoodInfo всегда делится на ненулевое число.

# Примечание 2. Если объект, с которым выполняется арифметическая операция, 
# некорректен, метод, реализующий эту операцию, должен вернуть константу 
# NotImplemented.

# Примечание 3. Никаких ограничений касательно реализации класса FoodInfo нет, 
# она может быть произвольной.


# Sample Input 1:

# food1 = FoodInfo(10, 20, 30)
# food2 = FoodInfo(10, 10, 20)

# print(food1 + food2)
# print(food1 * 2)
# print(food1 / 2)
# print(food1 // 2)

# Sample Output 1:

# FoodInfo(20, 30, 50)
# FoodInfo(20, 40, 60)
# FoodInfo(5.0, 10.0, 15.0)
# FoodInfo(5, 10, 15)

# Sample Input 2:

# food1 = FoodInfo(10, 20, 30)

# try:
#     food2 = (5, 10, 15) + food1
# except TypeError:
#     print('Некорректный тип данных')

# Sample Output 2:

# Некорректный тип данных

##############################################################################################

class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f"FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})"

    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return FoodInfo(
                self.proteins + other.proteins,
                self.fats + other.fats,
                self.carbohydrates + other.carbohydrates,
            )
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            return FoodInfo(self.proteins * n, self.fats * n, self.carbohydrates * n)
        return NotImplemented

    def __truediv__(self, n):
        if isinstance(n, (int, float)):
            return FoodInfo(self.proteins / n, self.fats / n, self.carbohydrates / n)
        return NotImplemented

    def __floordiv__(self, n):
        if isinstance(n, (int, float)):
            return FoodInfo(self.proteins // n, self.fats // n, self.carbohydrates // n)
        return NotImplemented
