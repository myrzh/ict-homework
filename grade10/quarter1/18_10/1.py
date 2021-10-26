def is_prime(n): # функция определения простого числа
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

prime_numbers = []
prime_numbers_indexes = []
for i in range(2532000, 2532160 + 1):
    if is_prime(i):
        prime_numbers.append(i)

prime_numbers_indexes = list(range(1, len(prime_numbers) + 1))
for i in range(0, len(prime_numbers), 3):
    print(prime_numbers_indexes[i], prime_numbers[i])
