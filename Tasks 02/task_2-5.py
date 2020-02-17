#!/usr/bin/python3.8
#
#   task_2-5
#
# Создайте свой генератор seq(), который работает аналогично встроенной функции range().
# Подсказка – используйте значения по умолчанию None для параметров, чтобы различить вызов seq() с одним, двумя или тремя аргументами.
# Внимание: внутри функции seq() стандартный range() вызывать нельзя.


def seq(stop, start=None, step=None):
    if start:
        start, stop = stop, start
    else:
        start = 0

    if not step:
        step = 1

    while start < stop:
        yield start
        start += step


print("Call seq(6):")
for i in seq(6):
    print(i, end=' ')

print("\nCall seq(4, 10):")
for i in seq(4, 10):
    print(i, end=' ')

print("\nCall seq(4, 12, 3):")
for i in seq(4, 12, 3):
    print(i, end=' ')