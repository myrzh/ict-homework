def func(n_input: int) -> int:
    n_bin = bin(n_input)[2:]

    if n_input % 3 == 0:
        n_bin += n_bin[-3:]
        return int(n_bin, 2)
    if n_input % 3 != 0:
        n_bin += bin(n_input % 3 * 3)[2:]
        return int(n_bin, 2)


for i in range(500):
    f = func(i)
    if f < 100:
        print(i, f)
