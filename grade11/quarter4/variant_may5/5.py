def func(n_input: int) -> int:
    n_bin = f"{n_input - (n_input % 4):b}"
    n_bin += str(n_bin.count("1") % 2)
    n_bin += str(n_bin.count("1") % 2)
    return int(n_bin, 2)


for i in range(1, 5000):
    f = func(i)
    if f > 0:
        print(i, f)
