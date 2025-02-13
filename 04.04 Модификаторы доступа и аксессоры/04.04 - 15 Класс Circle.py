# "Поколение Python": ООП
# 4.4 Модификаторы доступа и аксессоры

# 15 - Класс Circle

# Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать один
# аргумент:
# radius — радиус круга

# Экземпляр класса Circle должен иметь три атрибута:
# _radius — радиус круга
# _diameter — диаметр круга
# _area — площадь круга

# Класс Circle должен иметь три метода экземпляра:
# get_radius() — метод, возвращающий радиус круга
# get_diameter() — метод, возвращающий диаметр круга
# get_area() — метод, возвращающий площадь круга

# Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, 
# что реализованный класс используется только с корректными данными.

# Тестовые данные:

# Sample Input 1:

# circle = Circle(1)

# print(circle.get_radius())
# print(circle.get_diameter())
# print(round(circle.get_area()))

# Sample Output 1:

# 1
# 2
# 3

# Sample Input 2:

# circle = Circle(5)

# print(circle.get_radius())
# print(circle.get_diameter())
# print(round(circle.get_area()))

# Sample Output 2:

# 5
# 10
# 79

################################################################################################

import math

class Circle:

    def __init__(self, radius):
        self._radius = radius
        self._diameter = 2 * radius
        self._area = math.pi * radius**2

    def get_radius(self):
        return self._radius
    
    def get_diameter(self):
        return self._diameter
    
    def get_area(self):
        return self._area