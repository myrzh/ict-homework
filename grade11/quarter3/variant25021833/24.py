even = ("2", "4")
odd = ("1", "3", "5")

with open("24.txt", encoding="utf8") as f:
    line = f.readline().strip()

index = 0
pairs_counter = 0
pairs_list = []
while index < len(line) - 1:
    if line[index] in even:
        print(line[index])
        if line[index + 1] in odd:
            pairs_counter += 1
            index += 2
            continue
        pairs_list.append(pairs_counter)
        pairs_counter = 0
        index += 1

print(max(pairs_list))
