# "Поколение Python": ООП
# 5.3 Сравнение объектов

# Класс Word

# Будем называть словом любую последовательность из одной или более латинских букв.

# Реализуйте класс Word, описывающий слово. При создании экземпляра класс должен принимать 
# один аргумент:
# word — слово

# Экземпляр класса Word должен иметь следующее формальное строковое представление:
# Word('<слово в исходном виде>')

# И следующее неформальное строковое представление:
# <слово, в котором первая буква заглавная, а все остальные строчные>

# Также экземпляры класса Word должны поддерживать между собой все операции сравнения 
# с помощью операторов ==, !=, >, <, >=, <=. Два слова считаются равными, если их длины 
# совпадают. Слово считается больше другого слова, если его длина больше.

# Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, 
# реализующий эту операцию, должен вернуть константу NotImplemented.

# Примечание 2. Никаких ограничений касательно реализации класса Word нет, она может быть 
# произвольной.


# Sample Input 1:

# print(Word('bee') == Word('hey'))
# print(Word('bee') < Word('geek'))
# print(Word('bee') > Word('geek'))
# print(Word('bee') <= Word('geek'))
# print(Word('bee') >= Word('gee'))

# Sample Output 1:

# True
# True
# False
# True
# True

# Sample Input 2:

# words = [Word('python'), Word('bee'), Word('geek')]

# print(sorted(words))
# print(min(words))
# print(max(words))

# Sample Output 2:

# [Word('bee'), Word('geek'), Word('python')]
# Bee
# Python

##############################################################################################

# Если есть __eq__, то __ne__ добавится автоматически
# Если есть __gt__, то __lt__ добавится автоматически
# Если есть __ge__, то __le__ добавится автоматически
class Word:
    def __init__(self, word):
        self.word = word

    def __str__(self):
        return self.word.title()
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.word}')"
    
    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Word):
            return len(self.word) > len(other.word)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Word):
            return len(self.word) >= len(other.word)
        return NotImplemented


# ИЛИ с помощью декоратора класса @total_ordering из модуля functools
# Нужно создать 2 метода:
# - __eq__
# - один из __lt__, __gt__, __le__, __ge__
# Остальные добавятся автоматически

# from functools import total_ordering

# @total_ordering
# class Word:
#     def __init__(self, word):
#         self.word = word

#     def __str__(self):
#         return self.word.capitalize()

#     def __repr__(self):
#         return f"Word('{self.word}')"

#     def __eq__(self, other):
#         if isinstance(other, Word):
#             return len(self.word) == len(other.word)
#         return NotImplemented

#     def __lt__(self, other):
#         if isinstance(other, Word):
#             return len(self.word) < len(other.word)
#         return NotImplemented