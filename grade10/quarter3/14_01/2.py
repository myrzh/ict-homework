def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


f = open('26-2.txt')
n, k = map(int, f.readline().split())
a = []
for i in range(n):
    a.append(int(f.readline()))
bubble_sort(a)
a = a[k:n-k]
print(a[len(a) - 1] , end = " ")
print(int(sum(a)/len(a)))