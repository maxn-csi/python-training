#!/usr/bin/python3.8
#
#   task_01
#
# Пользователь вводит строку из букв в нижнем регистре.
# Нужно посчитать, сколько в этой строке английских гласных букв.
# Корректность ввода не проверять

string = input("Please enter a string: ")
print()

count = 0

for char in string:
    if char in "aeiouy":
        count += 1

print (count, "Vowels are in there")