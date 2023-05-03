# 10000000000
#  1?2139***4


for l1 in range(0, 10):
    for l2 in list(range(0, 10)) + [""]:
        for l3 in list(range(0, 10)) + [""]:
            for l4 in list(range(0, 10)) + [""]:
                line = f"1{l1}2139{l2}{l3}{l4}4"
                numb = int(line)
                if numb % 2023 == 0:
                    print(numb, numb / 2023)
