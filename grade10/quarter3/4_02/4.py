import os


# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j + 1] :
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '26-70.txt')
with open(filename , 'r') as f:
    array = f.readlines()
for i in range(0, len(array)):
    array[i] = array[i].rstrip()

result = []
 
#  перебор всех сумм с помощью рекурсии
def ban(result, v, index, curSum):
    if index < len(v):
        curSum += v[index]
        r = index
        while r < len(v):
            print('YASS')
            r += 1
            if ban(result, v, r, curSum) > 0:
                result.append(ban(result, v, r, curSum))
    return curSum


# нахождение всех сумм элементов массива v
for y in range(len(array)):
    array[y] = int(array[y])
for i in range(len(array)):
    if ban(result, array, i, 0) > 0:
        result.append(ban(result, array, i, 0))
    if array[i] > 0:
        result.append(array[i])
print(result)