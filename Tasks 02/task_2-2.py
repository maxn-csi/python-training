#!/usr/bin/python3.8
#
#   task_2-2
#
# Функция получает на вход целое число в диапазоне от 1 до 365. Это номер дня в 2020 году.
# Функция возвращает строку «workday» для рабочих дней (пн-пт), строку «day off» для выходных,
# и None, если входное значение было некорректным.


def weekday(day):
    if 0 < day < 366:
        day = (day % 7 + 2) % 7
        if 0 < day < 6:
            return "workday"
        else:
            return "day off"
    else:
        return None


day = int(input("Please enter day number: "))
print(weekday(day))
