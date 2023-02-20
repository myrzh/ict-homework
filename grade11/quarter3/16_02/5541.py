f = [0] * 1500
f[1] = 1
for n in range(2, 1100):
    f[n] = n * f[n - 1] - 1

print(f[1000] // f[997])
print(997001999)

numb = 0.1
print("%.100f" % numb)
