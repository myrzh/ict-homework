# ВАРИАНТ 1
import random

a = int(input())
k = int(input())
array = [random.randint(-100, 100) for x in range(20)]
odd_sum = 0
indexes = []
positive_k_bool = False

for i in array:
    if i % 2 != 0:
        odd_sum += i
    if i > 0 and i % k == 0:
        positive_k_bool = True

for y in range(0, len(array)):
    if array[y] > a:
        indexes.append(y)

for j in range(0, k):
    array[j] = -1 * array[j]

print(odd_sum)
print(indexes)
print(positive_k_bool)
print(array)