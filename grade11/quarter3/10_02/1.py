def func(n_input):
    n = bin(n_input)[2:]
    if n.count("1") % 2 == 0:
        n = "1" + n[2:] + "0"
        return int(n, 2)
    if n.count("1") % 2 == 1:
        n = "11" + n[2:] + "1"
        return int(n, 2)


res_list = []
for i in range(1000):
    res = func(i)
    if res > 25:
        res_list.append((i, res))

min_tuple = min(res_list, key=lambda x: x[1])
print(min_tuple[0])
