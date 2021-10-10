n = int(input())
array = []
for i in range(n + 1):
    for j in range(i):
        array.append(i)
print(*array[0:n])