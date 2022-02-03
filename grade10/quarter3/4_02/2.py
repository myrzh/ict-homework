from math import sin


def f(x):
    return x ** 3 - 8 * x + 1 - sin(x)


def main():
    a, b = map(float, input('Введите границы интервала: ').split())
    error = float(input('Введите погрешность: '))
    steps = 0
    while True:
        steps += 1
        if b - a > error:
            x = (a + b) / 2
            if f(x) * f(b) <= 0:
                a = x
            else:
                b = x
        else:
            print(f'Решение: {round((a + b) / 2, 3)}')
            print(f'Число шагов: {steps}')
            break


main()