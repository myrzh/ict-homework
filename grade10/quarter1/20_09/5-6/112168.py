x, y = map(float, input().split())

if y >= x ** 2 - 2 and (y <= x or y <= - x):
     print('YES')
else:
     print('NO')