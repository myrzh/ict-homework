def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


f = open('26-1.txt')
summ, n = map(int, f.readline().split())
a = []
for i in range(n):
    a.append(int(f.readline()))
bubble_sort(a)
i = 0
sump = 0

while  sump < summ:
    i = i + 1
    sump = sump + a[i]
print (i - 1, end = ' ' )
sump = (sump - a[i]) - a[i-1]
sumr = summ - sump
try:
    a.index(sumr)
    print (sumr)
except: a.append(sumr)
bubble_sort(a)
print ( a[a.index(sumr) - 1] )
