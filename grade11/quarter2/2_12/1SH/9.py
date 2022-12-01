import sys
import math


count = 0
for line in sys.stdin:
    line = line.strip()
    numbs = [int(i) for i in line.split('	')]
    if not all([i > 10 for i in numbs]):
        continue
    max_numb = max(numbs)
    max_index = numbs.index(max_numb)
    del numbs[max_index]
    if max_numb ** 3 >= 2 * math.prod(numbs):
        count += 1

print(count)