pairs = []
with open("27_B.txt") as f:
    n = f.readline()
    for line in f.readlines():
        num_a, num_b = map(int, line.split())
        pairs.append((num_a, num_b))

summ = 0
current_min = 10**6
for pair in pairs:
    summ += max(pair)
    temp_diff = abs(pair[0] - pair[1])
    if temp_diff % 3 != 0:
        current_min = min(current_min, temp_diff)

if summ % 3 != 0:
    print(summ)
else:
    print(summ - current_min)
