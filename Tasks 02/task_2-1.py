#!/usr/bin/python3.8
#
#   task_2-1
#
# Функция получает на вход два числа.
# Если оба числа чётные, функция возвращает их произведение.
# Если оба числа нечётные, функция возвращает их сумму.
# Если одно число чётное, а второе нечётное – функция возвращает это нечётное число.


def numbers(values):
    if not any(map(lambda x: x % 2, values)):
        res = 1
        for i in values:
            res *= i
        print("All even, product is: ", res)
    elif all(map(lambda x: x % 2, values)):
        print("All odd, sum is: ", sum(values))
    else:
        value_odd = filter(lambda x: x % 2 != 0, values)
        print(*value_odd, "is odd")


print("Please enter two numbers separated by space: ")

values = input().split()
values = list(map(int, values))

numbers(values)