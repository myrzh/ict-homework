arr = []
with open("tasks/17.txt", encoding="utf8") as f:
    for line in f.readlines():
        arr.append(int(line.strip()))

suitable_pairs = []
for i in range(len(arr) - 1):
    first = arr[i]
    second = arr[i + 1]
    if str(first)[-1] == "5" and str(second)[-1] == "5":
        suitable_pairs.append((first, second))

print(len(suitable_pairs))
maxx = max(suitable_pairs, key=lambda x: abs(x[0] - x[1]))
print(abs(maxx[0] - maxx[1]))
