for x in list(range(0, 10)) + ["A", "B", "C", "D", "E"]:
    n1 = int(f"123{x}5", 15)
    n2 = int(f"1{x}233", 15)
    n = n1 + n2
    if n % 14 == 0:
        print(x)
        print(n / 14)
        break
