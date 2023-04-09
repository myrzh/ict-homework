def func(n_input: int) -> int:
    n_bin = bin(n_input)[2:]

    if n_input % 3 == 0:
        print(n_bin)
        n_bin += n_bin[-3:]
        print(n_bin)
        return int(n_bin, 2)
    if n_input % 3 != 1:
        print(n_bin)
        n_bin += bin(n_input % 3 * 3)[2:]
        print(n_bin)
        return int(n_bin, 2)


print(func(10))
# for i in range(500):
#     print(i, func(i))
