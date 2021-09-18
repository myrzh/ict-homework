x, y = map(float, input().split())

if  (x ** 2 + y ** 2 <= 1) or (x >= 0 and x <= 1 and y >= 0 and y <= 1):    
    print('YES')
else:
    print('NO')