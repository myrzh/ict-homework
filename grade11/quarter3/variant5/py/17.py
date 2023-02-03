array = []
with open('17.txt') as f:
    for line in f.readlines():
        array.append(int(line.strip()))

suitable_pairs = []
for i in range(0, len(array) - 1):
    if array[i] + array[i + 1] >= 50:
        if array[i] >= 0 and array[i + 1] >= 0:
            suitable_pairs.append((array[i], array[i + 1]))

print(len(suitable_pairs))
best = min(suitable_pairs, key=lambda x: x[0] * x[1])
print(best[0] * best[1])