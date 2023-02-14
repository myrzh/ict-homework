def func(n_input):
    n = bin(n_input)[2:]
    if n.count("1") % 2 == 0:
        n = "1" + n[2:] + "0"
    elif n.count("1") % 2 == 1:
        n = "11" + n[2:] + "1"
    return int(n, 2)


suitable_pairs = []
for n in range(0, 100):
    r = func(n)
    if r > 25:
        suitable_pairs.append((n, r))

print(min(suitable_pairs, key=lambda x: x[1]))
