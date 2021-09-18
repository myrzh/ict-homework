x, y = map(float, input().split())

if x ** 2 + y ** 2 <= 1 and (y >= - x or y <= x):
    print('YES')
else:
    print('NO')