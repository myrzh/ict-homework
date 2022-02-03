from math import sin


def f(x):
    return x ** 3 - 8 * x + 1 - sin(x)


steps = 0


def get_solutions(start, end, error=0.001):
    global steps
    steps += 1
    if end - start <= error:
        return round((start + end) / 2, 3)
    x = (start + end) / 2
    if f(x) * f(end) <= 0:
        start = x
    else:
        end = x
    return get_solutions(start, end, error)


def main():
    start, end = map(float, input('Введите границы интервала: ').split())
    error = float(input('Введите погрешность: '))
    print(f'Решение: {get_solutions(start, end, error)}')
    print(f'Число шагов: {steps}')


main()