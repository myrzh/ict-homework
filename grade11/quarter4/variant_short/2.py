def func(n_input: int) -> int:
    n_str = str(n_input)
    numbs = [int(n_str[i] + n_str[i + 1]) for i in range(len(n_str) - 1)]
    return min(numbs) + max(numbs)


for i in range(10, 1000):
    r = func(i)
    if r == 137:
        print(i, r)
        break
