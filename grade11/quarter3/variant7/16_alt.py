k = 0
f = [1] * 1000
for n in range(39, 122):
    if n % 4 == 0:
        f[n] = n - f[n // 4] - f[n - 3]
    else:
        f[n] = 2 + f[n - 1] + f[n // 5]

for x in range(40, 121):
    if 60 < f[n] <= 240:
        k += 1
    print(k)
