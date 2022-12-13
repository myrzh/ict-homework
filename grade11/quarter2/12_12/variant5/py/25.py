def is_prime(numb):
    for i in range(2, numb // 2 + 1):
        if numb % i == 0:
            # print(i)
            return False
    return True


def greatest_divider(numb):
    if is_prime(numb):
        return 1
    for i in range(numb // 2 + 1, 0, -1):
        if numb % i == 0:
            return i

count = 0
number = 550001
while True:
    if count > 5:
        break
    if not is_prime(greatest_divider(number)):
        print(number, greatest_divider(number))
        # print(greatest_divider(number))
        # print(is_prime(greatest_divider(number)))
        # print()
        count += 1
    number += 1
