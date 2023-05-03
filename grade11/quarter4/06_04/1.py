def is_prime(number: int) -> bool:
    if number == 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def greatest_divider(number: int) -> int:
    if is_prime(number):
        return 1
    for i in range(number - 1, 1, -1):
        if number % i == 0:
            return i


counter = 0
start_number = 670_001
while counter < 6:
    if is_prime(start_number):
        start_number += 1
        continue
    if not is_prime(greatest_divider(start_number)):
        print(start_number, greatest_divider(start_number))
        counter += 1
        start_number += 1
        continue
    start_number += 1
