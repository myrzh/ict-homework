def func(s: str) -> str:
    while not "00" in s:
        s = s.replace("021", "102", 1)
        s = s.replace("022", "301", 1)
        s = s.replace("02", "20", 1)
        s = s.replace("01", "10", 1)
    return s


for n in range(1, 1000):
    for m in range(1, 1000):
        s = "0" + "1" * n + "2" * m + "0"
        res = func(s)
        if res.count("1") == 27 and res.count("2") == 9 and s.count("3") == 4:
            print(m)
            break
