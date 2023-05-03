# 10000000
#  3***52?


suitable_pairs = 0
for p1 in list(range(0, 10)) + [""]:
    for p2 in list(range(0, 10)) + [""]:
        for p3 in list(range(0, 10)) + [""]:
            for p4 in range(0, 10):
                numb_str = f"3{p1}{p2}{p3}52{p4}"
                if int(numb_str) ** 0.5 == int(int(numb_str) ** 0.5):
                    for i in range(int(numb_str) - 1, 1, -1):
                        if int(numb_str) % i == 0:
                            print(numb_str, i)
                            break
