def func(n_input):
    n = n_input - (n_input % 8) + (n_input % 2)
    n = bin(n)[2:]
    n_digits = [int(i) for i in n]
    n += str(sum(n_digits) % 2)
    n_digits = [int(i) for i in n]
    n += str(sum(n_digits) % 2)
    return int(n, 2)


for i in range(0, 200):
    print(func(i))