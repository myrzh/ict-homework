def dell(n, m):
    return n % m == 0


def func(x, a):
    return (not (dell(x, a))) <= (dell(x, 18) <= (not (dell(x, 81))))


for a in range(1000, 0, -1):
    flag = True
    for x in range(0, 1000):
        f = func(x, a)
        if not f:
            flag = False
            break
    if flag:
        print(a)
        break
