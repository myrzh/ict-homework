for x in list(range(0, 10)) + ["A", "B", "C", "D", "E"]:
    numb1 = int(f"97968{x}13", 15)
    numb2 = int(f"7{x}213", 15)
    summ = numb1 + numb2
    if summ % 14 == 0:
        print(x)
        print(summ / 14)
        break
