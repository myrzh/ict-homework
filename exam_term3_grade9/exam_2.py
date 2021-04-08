# ВАРИАНТ 2

import random

array = [random.randint(-100, 100) for x in range(25)]
a = int(input('Введите a: '))
k = int(input('Введите k: '))
odd_sum = 0
div5_a_count = 0
negative_index = -1

for i in range(0, len(array)):
    if i % 2 != 0:
        odd_sum += array[i]
    if array[i] > a and array[i] % 5 == 0:
        div5_a_count += 1
    if array[i] < 0 and array[i] % 5 == 2:
        negative_index = i
        print(array[i])

# ВОТ ТУТ ЕСТЬ НЕКОТОРАЯ НЕУВЕРЕННОСТЬ, ТАК КАК ЗАДАНИЕ НЕ СОВСЕМ ПОНЯТО
array[k] = 1 / array[k]
array[k+1] = 1 / array[k+1]
# КОНЕЦ НЕУВЕРЕННОЙ ЧАСТИ

print('Задание 1, пункт 1:', odd_sum)
print('Задание 1, пункт 2:', div5_a_count)
print('Задание 2:', negative_index)
print('Задание 4:', array)

# ЗАДАНИЯ 3 И 5 НЕ СДЕЛАНЫ