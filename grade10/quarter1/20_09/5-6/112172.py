x, y = map(float, input().split())

if  ((x ** 2 + y ** 2 <= 1 or y >= x - 1) and x >= 0 and y <= 1):
    print('YES')
else:
    print('NO')