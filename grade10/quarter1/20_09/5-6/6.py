x, y = map(float, input().split())

if (y <= x ** 2 and x >= 2 - x) or (y <= x ** 2 and y <= 4 - x ** 2 and y <= 2 - x and x <= 0) or (y <= 2 - x and y <= x ** 2 and y >= 0) or (y <= x ** 2 and y >= 4 - x ** 2 and x >= 1):
    print('YES')
else:
    print('NO')