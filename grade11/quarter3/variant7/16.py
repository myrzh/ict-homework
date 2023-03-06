def func(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        if n % 4 == 0:
            return n - func(n // 4) - func(n - 3)
        return 2 + func(n - 1) + func(n // 5)
    return 0


counter = 0
for n in range(40, 120 + 1):
    if 60 < func(n) <= 240:
        counter += 1

print(counter)
