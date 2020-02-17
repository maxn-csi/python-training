#!/usr/bin/python3.8
#
#   task_03
#
# Пользователь вводит две строки. Программа выводит совпадающие буквы двух строк и их позиции в каждой строке. Считать, что позиции начинаются с 1.
# Пример: первая строка «alexey», вторая строка «volosevich»
# Вывод программы:
# l – первая строка = 2, вторая строка = 3
# e – первая строка = 3, вторая строка = 6
# e – первая строка = 5, вторая строка = 6

strnig1 = input("Enter the first string: ")
strnig2 = input("Enter the second string: ")
print()

for i in range(len(strnig1)):
    for j in range(len(strnig2)):
        if strnig1[i] == strnig2[j]:
            print(strnig1[i], "– первая строка =", i + 1, "вторая строка =", j + 1)