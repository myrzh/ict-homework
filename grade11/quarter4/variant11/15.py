def dell(n, m):
    return n % m == 0


def func(x, a):
    return (dell(x, 2) <= (not dell(x, 3))) or ((x + a) >= 100)


for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not func(x, a):
            flag = False
            break
    if flag:
        print(a)
        break
