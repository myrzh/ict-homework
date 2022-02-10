from math import *


def f2(x):
    return 0


a, b = map(float, input('Введите границы трапеции: ').split())
func = input('Введите функцию, ограничивающую трапецию: ')
h = float(input('Введите шаг дискретизации: '))


def f1(x):
    return eval(func)


s = 0
x = a
while x < b:
    s += f1(x) - f2(x) + f1(x + h) - f2(x + h)
    x += h
s *= h / 2
print(f'Площадь трапеции: {round(s, 3)}')