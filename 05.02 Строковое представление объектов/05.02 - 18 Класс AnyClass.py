# "Поколение Python": ООП
# 5.2 Строковое представление объектов

# Класс AnyClass

# Реализуйте класс AnyClass. При создании экземпляра класс должен принимать произвольное 
# количество именованных аргументов и устанавливать их в качестве атрибутов создаваемому 
# экземпляру.

# Экземпляр класса AnyClass должен иметь следующее формальное строковое представление:

# AnyClass(<имя 1-го атрибута>=<значение 1-го атрибута>, <имя 2-го атрибута>=<значение 2-го атрибута>, ...)

# И следующее неформальное строковое представление:

# AnyClass: <имя 1-го атрибута>=<значение 1-го атрибута>, <имя 2-го атрибута>=<значение 2-го атрибута>, ...

# Примечание 1. Обратите внимание, что значения атрибутов, которые принадлежат типу str, 
# должны быть обрамлены апострофами.

# Примечание 2. Никаких ограничений касательно реализации класса AnyClass нет, она может быть 
# произвольной.


# Sample Input 1:

# any = AnyClass()

# print(str(any))
# print(repr(any))

# Sample Output 1:

# AnyClass: 
# AnyClass()

# Sample Input 2:

# cowboy = AnyClass(name='John', surname='Marston')

# print(str(cowboy))
# print(repr(cowboy))

# Sample Output 2:

# AnyClass: name='John', surname='Marston'
# AnyClass(name='John', surname='Marston')

# Sample Input 3:

# obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)

# print(str(obj))
# print(repr(obj))

# Sample Output 3:

# AnyClass: attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None
# AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)

##############################################################################################


class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__ |= kwargs

    def __str__(self):
        tmp = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"AnyClass: {', '.join(tmp)}"

    def __repr__(self):
        tmp = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"{self.__class__.__name__}({', '.join(tmp)})"
