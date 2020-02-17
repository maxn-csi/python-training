#!/usr/bin/python3.8
#
#   task_2-3
#
# Функция получает на вход произвольное количество строк и склеивает их все в одну строку.
# Опциональный именованный параметр – строка-разделитель, вставляемая между склеиваемыми строками (по умолчанию это пробел).

delim = input("Specify delimiter (optional): ")
print("Enter a few strings. Put empty string to proceed: ")

lines = []

while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break


def concat(args, delim_arg):
    newString = ""
    if delim_arg == "": delim_arg = " " 
    for i in range(len(args)):
        if i == len(args) - 1: delim_arg = ""
        newString += args[i] + delim_arg
    print(newString)


concat(lines, delim)