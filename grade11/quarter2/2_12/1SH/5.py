def func(n_input):
    n = bin(n_input)[2:]
    if n[-1] == '0':
        n = '10' + n
    else:
        n = '1' + n + '01'
    return int(n, 2)


for i in range(0, 100):
    result = func(i)
    print(i, result)
    if result >= 19:
        break
