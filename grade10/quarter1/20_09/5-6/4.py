x, y = map(float, input().split())

if (y <= x ** 2 and y <= 2 - x and y >= 0) or (y <= x ** 2 and y >= 2 - x):
    print('YES')
else:
    print('NO')