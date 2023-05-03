def func(x, A):
    P = list(range(6, 45 + 1))
    Q = list(range(18, 52 + 1))
    return ((x in Q) == (x in P)) or (((x in P) and (x not in Q)) <= (x in A))


A = list(range(6, 17 + 1))
flag = True
for x in range(0, 1000):
    f = func(x, A)
    if not f:
        flag = False
        break
if flag:
    print("YES")
