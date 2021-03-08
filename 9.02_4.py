# ВАРИАНТ 4
# ВВОД МАССИВА ЧЕРЕЗ ПРОБЕЛЫ ОДНОЙ СТРОКОЙ
# НОМЕРА ЭЛЕМЕНТОВ МАССИВА СЧИТАЮТСЯ С 0 (ДЛЯ ЗАДАНИЯ 3)

"""
ПРИМЕР ВВОДА-ВЫВОДА:

INPUT:
-4 -2 -1 4 4 6 3 -9
5
3

OUTPUT:
-16
3
True
[-4, 1, -1, 9, 4, 25, 3, 49]
"""

array = input().split()
a = int(input())
k = int(input())
negative_sum = 0
positive_a_count = 0
negative_k_bool = False

for x in range(0, len(array)):
    array[x] = int(array[x])

for i in array:
    if i < 0:
        negative_sum += i
    if i > 0 and i < a:
        positive_a_count += 1
    if i < 0 and i % k == 0:
        negative_k_bool = True

for j in range(0, len(array)):
    if j % 2 != 0:
        array[j] = j ** 2

print(negative_sum)
print(positive_a_count)
print(negative_k_bool)
print(array)