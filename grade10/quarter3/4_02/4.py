from random import randint


def bin_search_steps(numbs_list, number_to_find):
    steps = 0
    left = 0
    right = len(numbs_list) - 1
    while left <= right:
        steps += 1
        middle = left + (right - left) // 2
        if numbs_list[middle] == number_to_find:
            return steps
        elif numbs_list[middle] < number_to_find:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [randint(0, 100) for i in range(32)]
bubble_sort(arr)
steps_list = []

for i in [randint(0, 100) for x in range(1000)]:
    new_steps = bin_search_steps(arr, i)
    if new_steps != -1:
        steps_list.append(new_steps)

print(sum(steps_list) / len(steps_list))