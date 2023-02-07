min_n = 0
min_r = 0


flag = False
for i in range(100):
    n = bin(i)[2:]

    if n.count("1") % 2 == 0:
        n = "1" + n[2:] + "0"
    elif n.count("1") % 2 == 1:
        n = "11" + n[2:] + "1"
    r = int(n, 2)

    if r > 25:
        if not flag:
            min_r = r
            flag = True
        else:
            if r <= min_r:
                min_n = i
                min_r = r

print(min_n)
