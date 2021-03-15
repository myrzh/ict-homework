# ВАРИАНТ 4

array = input('Введите массив: ').split()
a = int(input('Введите a: '))
k = int(input('Введите k: '))
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

print('Задание 1, пункт 1:', negative_sum)
print('Задание 1, пункт 2:', positive_a_count)
print('Задание 2:', negative_k_bool)
print('Задание 3:', array)