vowels = "EI"
cons = "FGH"

with open("tasks/24(15).txt", encoding="utf8") as f:
    line = f.readline().strip()

index = 0
pairs_counter = 0
pairs_list = []
while index < len(line) - 1:
    if line[index] in vowels:
        if line[index + 1] in vowels:
            pairs_counter += 1
            index += 2
            continue
        pairs_list.append(pairs_counter)
        pairs_counter = 0
        index += 1
        continue
    if line[index] in cons:
        if line[index + 1] in cons:
            pairs_counter += 1
            index += 2
            continue
        pairs_list.append(pairs_counter)
        pairs_counter = 0
        index += 1
        continue

print(max(pairs_list))
