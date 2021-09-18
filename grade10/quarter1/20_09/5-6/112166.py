from math import sin, pi


x, y = map(float, input().split())

if y >= 0 and y <= 0.5 and y <= sin(x) and x >= 0 and x <= pi:
    print('YES')
else:
    print('NO')