from itertools import permutations


sixlets = []
with open("tasks/9.txt", encoding="utf8") as f:
    for line in f.readlines():
        sixlets.append([int(i) for i in line.strip().split()])

count = 0
for sixlet in sixlets:
    if len(set(sixlet)) == 5:
        if any(sum(arr[:3]) == sum(arr[3:]) for arr in permutations(sixlet)):
            count += 1

print(count)
