with open("tasks/17.txt", encoding="utf8") as f:
    numbers = []
    for line in f.readlines():
        numbers.append(int(line.strip()))

for i in sorted(numbers):
    if i % 8 == 0 and i != 8:
        min8 = i
        break

suitable_pairs = []
for i in range(len(numbers) - 1):
    first = numbers[i]
    second = numbers[i + 1]
    if first % min8 == 0 and second % min8 == 0:
        suitable_pairs.append((first, second))

print(len(suitable_pairs), max(min(suitable_pairs, key=sum)))
