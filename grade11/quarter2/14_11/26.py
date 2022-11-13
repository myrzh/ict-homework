rads = sorted([int(input()) for _ in range(int(input()))], reverse=True)

towers = []
for begin_index in range(0, len(rads)):
    tower = [rads[begin_index]]
    for index in range(begin_index + 1, len(rads)):
        if tower[-1] - rads[index] >= 7:
            tower.append(rads[index])
    towers.append(tower)

the_best = max(towers, key=len)
print(len(the_best), the_best[-1])
