#!/usr/bin/python3.8
#
#   task_3-1
#
# Создайте класс Color для представления цвета в цветовой модели RGB (https://ru.wikipedia.org/wiki/RGB).
# При создании объекта класса Color задаются значения трёх цветовых компонент R G и B.
# Значения должны быть целыми числами и лежать в диапазоне от 0 до 255.
# Если это не так, значение усекается до границы диапазона (например, значение -2 становится 0, а значение 300 становится 255).
# Класс Color должен иметь методы для получения каждого цветового компонента объекта в виде числа,
# а также метод для получения строкового представления цвета (например, в виде "R=100 G=255 B=0").
# Добавьте в класс Color метод для вычисления яркости по формуле:
# Y = 0.299R + 0.587G + 0.114B
# Два цвета называются совместимыми, если их яркости различаются больше, чем на 128.
# Добавьте в класс Color метод для проверки совместимости двух цветов.

# Class definition -------------------------------------------------------

class Color():
    def __init__(self, r, g, b):
        def clamp(x):
            return max(min(x, 255), 0)
        self.r = clamp(r)
        self.g = clamp(g)
        self.b = clamp(b)
        self.luminance()

    def __repr__(self):     # print in hex
        return "#{0:02x}{1:02x}{2:02x}".format(self.r, self.g, self.b)

    def red(self):
        return self.r

    def green(self):
        return self.g

    def blue(self):
        return self.b

    def text(self):
        return "R=" + str(self.r) + " G=" + str(self.g) + " B=" + str(self.b)

    def luminance(self):
        self.y = 0.299 * self.r + 0.587 * self.g + 0.114 * self.b
        return self.y

    def compare(self, color2):
        return abs(self.luminance() - color2.luminance()) > 128

# Demo -------------------------------------------------------

def main():
    newColor = Color(-100, 128, 300)
    newColor2 = Color(0, 255, 255)

    # Output
    print(newColor.text())  # строковоe представлениe цвета
    print(newColor.red())   # метод для получения цветового компонента объекта в виде числа
    print(newColor.y)       # метод для вычисления яркости
    print(newColor.compare(newColor2))  # метод для проверки совместимости двух цветов
    # print(newColor)       # test hex output

main()
