# "Поколение Python": ООП
# 4.7 Декораторы @classmethod и @staticmethod

# Класс Rectangle

# Реализуйте класс Rectangle, описывающий прямоугольник. При создании экземпляра класс должен 
# принимать два аргумента в следующем порядке:
# length — длина прямоугольника
# width — ширина прямоугольника

# Экземпляр класса Rectangle должен иметь два атрибута:
# length — длина прямоугольника
# width — ширина прямоугольника

# Класс Rectangle должен иметь один метод класса:
# square() — метод, принимающий в качестве аргумента число side и возвращающий экземпляр 
# класса Rectangle c длиной и шириной, равными side

# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, 
# что реализованный класс используется только с корректными данными.

# Sample Input 1:

# rectangle = Rectangle(4, 5)

# print(rectangle.length)
# print(rectangle.width)

# Sample Output 1:

# 4
# 5

# Sample Input 2:

# rectangle = Rectangle.square(5)

# print(rectangle.length)
# print(rectangle.width)

# Sample Output 2:

# 5
# 5

##############################################################################################

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @classmethod
    def square(cls, side):
        return cls(side, side)
