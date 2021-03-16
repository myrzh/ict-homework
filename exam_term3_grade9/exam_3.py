# ВАРИАНТ 3

array = input('Введите массив: ').split()
a = int(input('Введите число: '))
positive_sum = 0
div_3_5 = []
div_a = False

for x in range(0, len(array)):
    array[x] = int(array[x])

for i in range(0, len(array)):
    if array[i] > 0 and array[i] < 10:
        positive_sum += array[i]
    if array[i] % 3 == 0 and array[i] % 5 == 0:
        div_3_5.append(i)

for j in range(0, len(array)):
    if array[j] + array[j+1] == a:
        div_a = True
        break

for y in range(0, len(array)):
    if array[y] % 3 == 0:
        array[y] = array[y] * array[2]

print('Задание 1, пункт 1:', positive_sum)
print('Задание 1, пункт 2:', div_3_5)
print('Задание 2:', div_a)
print('Задание 3:', array)