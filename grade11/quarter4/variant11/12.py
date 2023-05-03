def is_prime(number: int) -> bool:
    if number == 1:
        return False
    for r in range(2, int(number**0.5) + 1):
        if number % r == 0:
            return False
    return True


for n in range(1, 1000):
    s = ">" + "0" * 39 + "1" * n + "2" * 39
    while ">1" in s or ">2" in s or ">0" in s:
        if ">1" in s:
            s = s.replace(">1", "22>", 1)
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        if ">0" in s:
            s = s.replace(">0", "1>", 1)
    summ = 0
    for i in s:
        if i.isdigit():
            summ += int(i)
    if is_prime(summ):
        print(n)
        break
