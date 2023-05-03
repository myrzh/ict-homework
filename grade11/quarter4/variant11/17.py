numbers = []
with open("tasks/17.txt", encoding="utf8") as f:
    for line in f.readlines():
        numbers.append(int(line.strip()))

three_max = max(list(filter(lambda x: str(x)[-1] == "3", numbers)))

suitable_pairs = []
for i in range(len(numbers) - 1):
    first = numbers[i]
    second = numbers[i + 1]
    if (str(first)[-1] == "3") ^ (str(second)[-1] == "3"):
        if (first**2 + second**2) >= three_max**2:
            suitable_pairs.append((first, second))

print(len(suitable_pairs))
maxx = max(suitable_pairs, key=lambda x: x[0] ** 2 + x[1] ** 2)
print(maxx[0] ** 2 + maxx[1] ** 2)
