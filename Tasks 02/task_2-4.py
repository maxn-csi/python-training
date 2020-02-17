#!/usr/bin/python3.8
#
#   task_2-4
#
# Создайте свою реализацию стандартной функции filter(). Функции передаётся итерируемый объект и предикат фильтрации.
# На выходе – набор значений, прошедших фильтрацию.
# В процессе работы функция filter() должна печатать значения, прошедшие фильтрацию. Оформите filter() как генератор.


def filter(iterable, condition):
    for element in iterable:
        if condition(element):
            print(element)
            yield element


range_lim = input("Enter <int> range limit to create iterable object: ")
iter_list = range(int(range_lim))


# calling filter() to generate and return values
for item in filter(iter_list, lambda x: x % 2 == 0): pass
