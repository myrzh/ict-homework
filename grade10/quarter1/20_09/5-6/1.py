x, y = map(float, input().split())

if x <= 2 and y <= x and y >= x ** 2 + y ** 2:
    print('YES')
else:
    print('NO')