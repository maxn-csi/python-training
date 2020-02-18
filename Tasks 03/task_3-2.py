#!/usr/bin/python3.8
#
#   task_3-2
#
# Создайте класс Picture для представления растровых картинок. Объект Picture просто хранит набор точек.
# У точки задаются числовые координаты X и Y и значение Color (этот тип вы создали в задании 1).
# У класса Picture должны быть методы для добавления точки по координатам и для удаления точки по координатам.
# Снабдите класс Picture методом для поиска координат самой яркой точки картинки.

import random   # используется для заполнения изображения случайными точками

# Color class -------------------------------------------------------

class Color():
    def __init__(self, r, g, b):
        def clamp(x):
            return max(min(x, 255), 0)
        self.r = clamp(r)
        self.g = clamp(g)
        self.b = clamp(b)
        self.luminance()

    def __repr__(self):     # вывод в hex виде, для print()
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

# Picture class -------------------------------------------------------

class Picture():

    points = [[]]

    def __init__(self, width, height):
        for x in range(width):
            self.points.append(list())
            for y in range(height):
                self.points[x].append(list())
                self.points[x][y] = Color(0, 0, 0)

    def add_point(self, x, y, color):   # добавление точки по координатам
        self.points[x - 1][y - 1] = color

    def del_point(self, x, y):          # удаление точки по координатам
        self.points[x - 1][y - 1] = Color(0, 0, 0)

    def randomize(self):                # заполнение точками случайного цвета
        def rand_color():
            return random.randint(0, 255)
        for i in range(len(self.points)):
            for j in range(len(self.points[i])):
                self.points[i][j] = Color(
                    rand_color(), rand_color(), rand_color())

    def brightest(self):                # поиск координат самой яркой точки
        actual = [0, 0, self.points[0][0].luminance()]
        for i in range(len(self.points)):
            for j in range(len(self.points[i])):
                candidate = self.points[i][j].luminance()
                if candidate > actual[2]:
                    actual = [i, j, candidate]
        return "The brightes point is at: X " + str(actual[0] + 1) + ", Y " + str(actual[1] + 1)

# Demo -------------------------------------------------------

pict = Picture(10, 10)
pict.randomize()
# pict.add_point(10, 10, Color(255, 255, 255))
# pict.del_point(1, 1)
# print(pict.points)        # debug output
print(pict.brightest())
