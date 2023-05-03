def func(a, x):
    return (x in list(range(160, 181))) <= ((x % 35 == 0) <= (x % a == 0))


count = 0
for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not func(a, x):
            flag = False
            break
    if flag:
        count += 1

print(count)
