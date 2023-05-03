f = [0] * 21_000
for n in range(10_000, 20_000):
    f[n] = n
for n in range(10_000, 0, -1):
    if n % 2 == 0:
        f[n] = f[n + 2] - 3
    else:
        f[n] = f[n + 2] + 1

print(f[94] - f[80])
