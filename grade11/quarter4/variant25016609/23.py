def func(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    return func(x - 2, y) + func(x // 2, y)


print(func(28, 10) * func(10, 1))
