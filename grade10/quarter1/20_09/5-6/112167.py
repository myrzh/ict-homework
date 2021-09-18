x, y = map(float, input().split())

if  y <= 2 - x**2 and (y >= 0 or  y >= x):
    print('YES')
else:
    print('NO')