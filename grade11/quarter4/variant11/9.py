from pprint import pprint
from collections import Counter


numbers_matrix = []
with open("tasks/9.txt", encoding="utf8") as f:
    while line := f.readline():
        line_list = line.strip().split()
        numbers_matrix.append(tuple(map(int, line_list)))

count = 0
for seq in numbers_matrix:
    if len(set(seq)) == 5:
        cnt = Counter(seq)
        rep_sum = 0
        nonrep_sum = 0
        # pprint(cnt)
        for key, value in cnt.items():
            if value == 1:
                nonrep_sum += key
            elif value == 2:
                rep_sum += key * 2
        if (nonrep_sum / 4) <= rep_sum:
            count += 1

print(count)
