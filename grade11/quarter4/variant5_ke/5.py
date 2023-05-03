def func(n_input: int) -> int:
    n_bin = f"{n_input:b}"
    if n_input % 2 == 0:
        n_bin = f"1{n_bin}00"
        return int(n_bin, 2)
    if n_input % 2 == 1:
        temp_summ = f"{n_bin.count('1'):b}"
        n_bin = f"{n_bin}{temp_summ}"
        return int(n_bin, 2)


for n in range(1, 5000):
    r = func(n)
    if r > 190:
        print(n, r)
