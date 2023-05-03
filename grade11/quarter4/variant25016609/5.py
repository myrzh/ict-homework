def func(n_input: int) -> int:
    n_bin = f"{n_input:b}"
    if n_bin.count("1") % 2 == 0:
        n_bin = "10" + n_bin[2:] + "1"
        return int(n_bin, 2)
    n_bin = "11" + n_bin[2:] + "0"
    return int(n_bin, 2)


for n in range(1, 16):
    print(n, func(n))
