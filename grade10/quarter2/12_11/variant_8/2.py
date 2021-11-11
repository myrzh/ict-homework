for i in range(777, 3777 + 1):
    if hex(i)[-1] == 'f' and hex(i)[2:][0] == 'a' and i % 11 != 0: print(i)