min_n = 0
min_r = 26


for i in range(100):
    n = bin(i)[2:]

    if n.count("1") % 2 == 0:
        n = "1" + n[2:] + "0"
    elif n.count("1") % 2 == 1:
        n = "11" + n[2:] + "1"
    r = int(n, 2)

    if r > 25:
        if r <= min_r:
            min_n = i

print(min_n)
