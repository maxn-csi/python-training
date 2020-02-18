#!/usr/bin/python3.8
#
#   task_3-3
#
# Класс Kelvin хранить температуру в кельвинах (атрибут value). Температура в кельвинах не может быть отрицательной.
# Определите в классе методы:
# · Для строкового представления температуры (100.6K).
# · Для истинности температуры (true, если температура отличается от 0 не более чем на 10Е-6).
# · Для сложения, вычитания температур, для умножения температуры на неотрицательное число.
# · Для сравнения температур (две температуры равны, если отличаются не более чем на 10Е-6)

# Kelvin class -------------------------------------------------------

class Kelvin():
    def __init__(self, value):
        self.value = max(value, 0)
        '''Температура в кельвинах не может быть отрицательной'''
        if value != self.value:
            print("Kelvin can't be negative! Setting to zero")

    def __repr__(self):    
        '''Строковое представление температуры'''
        return str(self.value) + "\u212A"

    def __bool__(self):
        '''Истинность температуры'''
        return self.value < 10e-6

    def __add__(self, other):  
        '''Сложение'''
        try:
            return Kelvin(self.value + other.value)
        except:
            return NotImplemented

    def __sub__(self, other):
        '''Вычитание'''
        try:
            return Kelvin(max(self.value - other.value, 0))
        except:
            return NotImplemented

    def __mul__(self, other):   
        '''Умножение'''
        if other >= 0:            
            try:
                return Kelvin(self.value * other)
            except:
                return NotImplemented
        else:
            return "Can't multiply by negative!"

    def __eq__(self, other):
        '''Сравнение'''
        return (max(self.value, other.value) - min(self.value, other.value)) < 10E-6

# Demo -------------------------------------------------------

temp1 = Kelvin(300.15)
temp2 = Kelvin(14e-7)
temp3 = Kelvin(15E-7)
temp_add = Kelvin(55)

print("Test print() output: " + str(temp1))
# print(temp1)

print("\nИстинность температуры. temp2(14e-7) < 10Е-6 ?: ")
print(True) if temp2 else print(False)
    
# print(bool(temp1))
# print(bool(temp2))

print("\nСравнение температур:")
print("temp1 == temp2 > " + str(temp1 == temp2))
print("temp2 == temp3 > " + str(temp2 == temp3))

print("\nСложение:")
print("temp1 + temp_add = " + str(temp1 + temp_add))

print("\nВычитание:")
print("temp1 - temp_add = " + str(temp1 - temp_add))
print("temp_add - temp1 = " + str(temp_add - temp1))

print("\nУмножение:")
print("temp_add * 2 = " + str((temp_add * 2)))
print("temp_add * -2 = " + str((temp_add * -2)))