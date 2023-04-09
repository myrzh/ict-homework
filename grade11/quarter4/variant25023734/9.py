with open("tasks/9.txt", encoding="utf-8") as f:
    numbers = []
    for line in f.readlines():
        temp_numbers = list(line.strip().split())
        temp_numbers = tuple(map(int, temp_numbers))
        numbers.append(temp_numbers)

count = 0
for seq in numbers:
    if len(set(seq)) == 5:
        temp_seq = list(seq[::])
        min_num = min(temp_seq)
        max_num = max(temp_seq)
        temp_seq.remove(min_num)
        temp_seq.remove(max_num)
        if (min_num + max_num) * 3 <= sum(temp_seq) * 2:
            count += 1

print(count)
