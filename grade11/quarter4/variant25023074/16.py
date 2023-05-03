f = [0] * 13_000
for n in range(0, 13_000):
    if n < 2:
        f[n] = 7
    elif n > 1:
        f[n] = 7 * f[n - 2]

print(f[12950] / (7**6473))
