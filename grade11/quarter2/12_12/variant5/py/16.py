F = [0] * 130
F[1] = 1
F[2] = 2
for n in range(3, 130):
    F[n] = n * (n - 1) * F[n - 1]
print(F[123] / F[120])