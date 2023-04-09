def func(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    if x == 13:
        return 0
    return func(x + 1, y) + func(x + 2, y) + func(x * 3, y)


print(func(3, 8) * func(8, 18))
