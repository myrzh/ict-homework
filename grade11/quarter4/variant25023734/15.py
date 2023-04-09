def func(x, a):
    return (x & 39 == 0) or ((x & 11 == 0) <= (not (x & a == 0)))


for a in range(0, 100):
    flag = True
    for x in range(0, 100):
        f = func(x, a)
        if not f:
            flag = False
    if flag:
        print(a)
        break
