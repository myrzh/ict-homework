def f(x, y, seq=""):
    if x == y:
        # print(seq)
        return 1
    if x > y:
        return 0
    if x == 28:
        return 0
    if "BACA" in seq:
        return 0
    return f(x + 2, y, seq + "A") + f(x + 3, y, seq + "B") + f(x * 2, y, seq + "C")


print(f(2, 40))
