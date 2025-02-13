# "Поколение Python": ООП
# 4.7 Декораторы @classmethod и @staticmethod

# Класс CaseHelper 🌶️🌶️

# Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом 
# нижнего подчеркивания (_) и не имеют пробелов в записи, причём каждое слово пишется с 
# маленькой буквы. Например, bee_geek и hello_world.

# Upper Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно 
# без пробелов, при этом каждое слово пишется с заглавной буквы. Например, BeeGeek и 
# HelloWorld.

# Реализуйте класс CaseHelper, описывающий набор функций для работы со строками в стилях 
# Snake Case и Upper Camel Case. При создании экземпляра класс не должен принимать никаких 
# аргументов.

# Класс CaseHelper должен иметь четыре статических метода:

# is_snake() — метод, принимающий в качестве аргумента строку и возвращающий True, если 
# переданная строка записана в стиле Snake Case, или False в противном случае
# is_upper_camel() — метод, принимающий в качестве аргумента строку и возвращающий True, 
# если переданная строка записана в стиле Upper Camel Case, или False в противном случае
# to_snake() — метод, который принимает в качестве аргумента строку в стиле Upper Camel Case,
# записывает ее в стиле Snake Case и возвращает полученный результат
# to_upper_camel() — метод, который принимает в качестве аргумента строку в стиле Snake Case, 
# записывает ее в стиле Upper Camel Case и возвращает полученный результат
# 
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, 
# что реализованный класс используется только с корректными данными.

# Sample Input 1:

# print(CaseHelper.is_snake('beegeek'))
# print(CaseHelper.is_snake('bee_geek'))
# print(CaseHelper.is_snake('Beegeek'))
# print(CaseHelper.is_snake('BeeGeek'))

# Sample Output 1:

# True
# True
# False
# False

# Sample Input 2:

# print(CaseHelper.is_upper_camel('beegeek'))
# print(CaseHelper.is_upper_camel('bee_geek'))
# print(CaseHelper.is_upper_camel('Beegeek'))
# print(CaseHelper.is_upper_camel('BeeGeek'))

# Sample Output 2:

# False
# False
# True
# True

# Sample Input 3:

# print(CaseHelper.to_snake('Beegeek'))
# print(CaseHelper.to_snake('BeeGeek'))

# Sample Output 3:

# beegeek
# bee_geek

# Sample Input 4:

# print(CaseHelper.to_upper_camel('beegeek'))
# print(CaseHelper.to_upper_camel('bee_geek'))

# Sample Output 4:

# Beegeek
# BeeGeek

##############################################################################################

# По ссылке https://inflection.readthedocs.io/en/latest/#module-inflection доступен модуль, который мог бы помочь решить задачу.

import re

class CaseHelper:
    @staticmethod
    def is_snake(string):
        pattern = r'[a-z]+(_[a-z]+)*'
        return bool(re.fullmatch(pattern, string))

    @staticmethod
    def is_upper_camel(string):
        pattern = r'([A-Z][a-z]+)+'
        return bool(re.fullmatch(pattern, string))
    
    @staticmethod
    def to_snake(string):
        # позиция в строке где: позади не начало строки, а впереди заглавная буква
        pattern = r"(?<!^)(?=[A-Z])"
        return re.sub(pattern, '_', string).lower()

    @staticmethod
    def to_upper_camel(string):
        # str.title() - возвр. стр. в которой все слова с заглавной буквы
        return string.title().replace('_', '')
