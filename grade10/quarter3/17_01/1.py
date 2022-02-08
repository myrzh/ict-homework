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


def main():
    print('Массив:')
    array = [int(i) for i in input().split()]
    bubble_sort(array)
    print('После сортировки:')
    print(*array)
    print('Введите число X:')
    numb = int(input())
    search_res = bin_search_steps(array, numb)
    if search_res == -1:
        print(f'Число {numb} не найдено.')
    else:
        print(f'Число {numb} найдено.')
        print(f'Количество сравнений: {search_res}')


if __name__ == "__main__":
    main()