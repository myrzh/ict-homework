import sys


numbs = []
for line in sys.stdin:
    line = line.strip()
    numbs.append(int(line))


suitable_pairs = []
for i in range(0, len(numbs)):
    new_numbs = numbs.copy()
    del new_numbs[i]
    for j in range(0, len(new_numbs)):
        one = numbs[i]
        two = new_numbs[j]
        if one + two % 120:
            suitable_pairs.append(one + two)

print(len(suitable_pairs), max(suitable_pairs))
