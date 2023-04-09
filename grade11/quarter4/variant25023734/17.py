with open("tasks/17.txt", encoding="utf-8") as f:
    numbers = []
    for line in f.readlines():
        numbers.append(int(line.strip()))


for number in numbers:
    if number in range(100, 1000):
        if number % 10 == 5:
            min_5 = number
            break

suitable_pairs = []
for index in range(len(numbers) - 1):
    first = numbers[index]
    second = numbers[index + 1]
    if (first in range(100, 1000) and second not in range(100, 1000)) or (
        first not in range(100, 1000) and second in range(100, 1000)
    ):
        if (first + second) % min_5 == 0:
            suitable_pairs.append((first, second))


print(len(suitable_pairs), sum(min(suitable_pairs, key=sum)))
