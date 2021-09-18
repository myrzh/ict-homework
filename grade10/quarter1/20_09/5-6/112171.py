x, y = map(float, input().split())

if (x >= 0 and x <= 1 and y >= 1 - x) or (y >= 1 - x and x < 0 and y > 2 * x ** 2):
    print('YES')
else:
    print('NO')