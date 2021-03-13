a = input().split()
for x in range(0, len(a)):
    a[x] = int(a[x])

count = 0

for i in range(0, len(array)):
    if i == 0:
        if a[i] > a[i + 1]:
            count += 1
    elif i == len(array) - 1:
        if a[i] > a[i - 1]:
            count += 1
    else:
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            count += 1

print(count)