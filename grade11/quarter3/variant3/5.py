def func(n_input):
    n = bin(n_input)[2:]
    if n.count('1') % 2 == 0:
        n = '1' + n[:-2] + '01'
    else:
        n = '1' + n[2:] + '10'
    return int(n, 2)


for i in range(1, 1000):
    print(func(i))
