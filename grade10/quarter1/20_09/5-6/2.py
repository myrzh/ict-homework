from math import sin, pi


x, y = map(float, input().split())

if y <= sin(x) and y >= 0 and y <= 0.5 and x >= 0 and x <= pi:
    print('YES')
else:
    print('NO')