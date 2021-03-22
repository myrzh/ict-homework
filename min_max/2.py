array = [int(i) for i in input().split()]

max_index = 0
count = 0

for i in range(1, len(array)):
    if array[i] > array[max_index]:
        max_index = i

for i in array:
    if i == array[max_index]:
        count += 1

print(count)