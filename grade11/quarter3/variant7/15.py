def exp(x, a):
    return ((x % a == 0) <= (not (x % 24 == 0) <= (not (x % 74 == 0)))) and (a > 500)


for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not exp(x, a):
            flag = False
            break
    if flag:
        print(a)
        break
