m, n = map(int, input().split())
x, y = map(int, input().split())
 
if y == 1:
    print(x, y + 1)
elif y == n:
    print(x, y - 1)
else:
    print(x, y - 1)
    print(x, y + 1)
if x == 1:
    print(x + 1, y)
elif x == m:
    print(x - 1, y)
else:
    print(x - 1, y)
    print(x + 1, y)

### NOT DONE