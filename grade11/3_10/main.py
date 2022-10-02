def func_1_2_3(r):
    r = bin(r)[2:]
    r += str(sum(int(i) for i in r) % 2)
    r += str(sum(int(i) for i in r) % 2)
    return int(r, 2)


def func_4(r):
    r = bin(r)[2:]
    if r.startswith('1'):
        r = r[1:]
    if r.count('1') % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '0'
    return int(r, 2)


def func_5(r):
    r = bin(r)[2:]
    if sum(int(i) for i in r) % 2 == 0:
        r += '0'
        r = '10' + r[2:]
    else:
        r += '1'
        r = '11' + r[2:]
    return int(r, 2)


def main():
    print(min(func_1_2_3(n) for n in range(-1000, 1000) if func_1_2_3(n) > 100))
    print(max(func_1_2_3(n) for n in range(-1000, 1000) if func_1_2_3(n) < 114))
    print(min(n for n in range(-1000, 1000) if func_1_2_3(n) > 125))
    print(max(func_4(n) for n in range(-1000, 1000) if func_4(n) < 450))
    print(min(n for n in range(-1000, 1000) if func_5(n) >= 16))


if __name__ == '__main__':
    main()