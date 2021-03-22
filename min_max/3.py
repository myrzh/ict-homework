# НЕДОДЕЛАНА

import random


array = [random.randint(100, 200) for i in range(20)]
sums = []
min_index = 0

for i in range(0, len(array) - 1):
    sums.append(array[i] + array[i + 1])

for i in range(1, len(sums)):
    if sums[i] > sums[min_index]:
        min_index = i

print()

# НЕДОДЕЛАНА