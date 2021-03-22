import random


array = [random.randint(50, 150) for x in range(20)]
min_index = 0
max_index = 0

for i in range(1, len(array)):
    if array[i] < array[min_index]:
        min_index = i
    if array[i] > array[max_index]:
        max_index = i

print("MIN: ", "A[", min_index, "] = ", array[min_index], sep="")
print("MAX: ", "A[", max_index, "] = ", array[max_index], sep="")