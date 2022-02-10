from random import randint


def bin_search(numbs_list, number_to_find):
    steps = 0
    left = 0
    right = len(numbs_list) - 1
    while left <= right:
        steps += 1
        middle = left + (right - left) // 2
        if numbs_list[middle] == number_to_find:
            return middle
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


def main():
    array = [randint(1, 100) for i in range(10)]
    print('Массив:')
    print(*array)
    bubble_sort(array)
    print('После сортировки:')
    print(*array)
    print('Введите число X:')
    numb = int(input())
    search_res = bin_search(array, numb)
    if search_res != -1:
        print(f'Число {numb} найдено.')
    else:
        array.append(numb)
        bubble_sort(array)
        x = bin_search(array, numb)
        if abs(array[x] - array[x + 1]) <= abs(array[x] - array[x - 1]):
            numb_new = array[x + 1] 
        else:
            numb_new = array[x - 1]
        print(f'Число {numb} не найдено. Ближайшее число {numb_new}')


if __name__ == "__main__":
    main()