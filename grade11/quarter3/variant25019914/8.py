def func(numb: str):
    if len(numb) != 6:
        return False
    return (
        (int(numb[0]) % 2 == 0 and int(numb[2]) % 2 == 0 and int(numb[4]) % 2 == 0)
        and (int(numb[1]) % 2 == 1 and int(numb[3]) % 2 == 1 and int(numb[5]) % 2 == 1)
    ) or (
        (int(numb[0]) % 2 == 1 and int(numb[2]) % 2 == 1 and int(numb[4]) % 2 == 1)
        and (int(numb[1]) % 2 == 0 and int(numb[3]) % 2 == 0 and int(numb[5]) % 2 == 0)
    )


count = 0
for one in range(1, 7):
    for two in range(0, 7):
        for three in range(0, 7):
            for four in range(0, 7):
                for five in range(0, 7):
                    for six in range(0, 7):
                        numb = "".join(map(str, [one, two, three, four, five, six]))
                        if func(numb) and numb.count("6") == 1:
                            print(numb)
                            count += 1

print(count)
