"""Особыми будем называть нетривиальные делители числа,
все цифры которых чётные. Нетривиальными считаются все делители,
кроме 1 и самого числа. Пусть D(N) – шестой по величине
(считая с наибольшего) особый делитель натурального числа N.
Если у числа N меньше 6 различных особых делителей,
то принимаем D(N) = 0. Найдите 5 наименьших натуральных чисел,
превышающих 400 000 000, для которых D(N) > 0. В ответе
запишите для каждого найденного N сначала значение D(N),
а затем общее количество особых делителей (в порядке
возрастания соответствующих чисел N).
"""


def is_prime(number: int) -> bool:
    if number == 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def sixth_greatest_divider(number: int) -> int:
    if is_prime(number):
        return 0
    for i in range(number - 1, 1, -1):
        if number % i == 0:
            return i


def is_special(numb: int) -> bool:
    return all(int(x) % 2 == 0 for x in str(numb))


count = 0
