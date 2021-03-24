import random


array = [random.randint(163, 190) for i in range(12)]
for i in range(len(array)):
    array[i] *= 2
print(*array)