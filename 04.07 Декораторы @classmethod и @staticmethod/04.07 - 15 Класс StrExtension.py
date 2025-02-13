# "Поколение Python": ООП
# 4.7 Декораторы @classmethod и @staticmethod

# Класс StrExtension

# Реализуйте класс StrExtension, описывающий набор функций для работы со строками. При 
# создании экземпляра класс не должен принимать никаких аргументов.

# Класс StrExtension должен иметь три статических метода:
# remove_vowels() — метод, который принимает в качестве аргумента строку, удаляет из нее все 
# гласные латинские буквы без учета регистра и возвращает полученный результат
# leave_alpha() — метод, который принимает в качестве аргумента строку, удаляет из нее все 
# символы, не являющиеся латинскими буквами, и возвращает полученный результат
# replace_all() — метод, который принимает три строковых аргумента string, chars и char, 
# заменяет в строке string все символы из chars на char с учетом регистра и возвращает 
# полученный результат.
# 
# Примечание 1. Гарантируется, что все буквенные символы относятся к латинскому алфавиту.

# Примечание 2. Латинские гласные буквы: a, e, i, o, u, y.

# Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, 
# что реализованный класс используется только с корректными данными.

# Sample Input 1:

# print(StrExtension.remove_vowels('Python'))
# print(StrExtension.remove_vowels('Stepik'))

# Sample Output 1:

# Pthn
# Stpk

# Sample Input 2:

# print(StrExtension.leave_alpha('Python111'))
# print(StrExtension.leave_alpha('__Stepik__()'))

# Sample Output 2:

# Python
# Stepik

# Sample Input 3:

# print(StrExtension.replace_all('Python', 'Ptn', '-'))
# print(StrExtension.replace_all('Stepik', 'stk', '#'))

# Sample Output 3:

# -y-ho-
# S#epi#

##############################################################################################

# 1 Вариант
from string import ascii_letters

class StrExtension:
    @staticmethod
    def remove_vowels(txt):
        vowels = 'aeiouyAEIOUY'
        return ''.join(el for el in txt if el not in vowels)

    @staticmethod
    def leave_alpha(txt):
        return ''.join(el for el in txt if el in ascii_letters)

    @staticmethod
    def replace_all(txt, chars, char):
        return ''.join(char if el in chars else el for el in txt)


# 2 Вариант. С рег. выр.
import re

class StrExtension:
    @staticmethod
    def remove_vowels(txt):
        pattern = r'[aeiouy]'
        return re.sub(pattern, '', txt, flags=re.I)
    
    @staticmethod
    def leave_alpha(txt):
        pattern = r'[^a-z]'
        return re.sub(pattern, '', txt, flags=re.I)
    
    @staticmethod
    def replace_all(txt, chars, char):
        pattern = rf'[{chars}]'
        return re.sub(pattern, char, txt)
