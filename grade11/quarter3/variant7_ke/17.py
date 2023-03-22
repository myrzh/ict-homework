f = open("tasks/17.txt")
s = [int(i.strip()) for i in f.readlines()]
f.close()
summ = 0
maxsumm = 0
k = 0
for i in range(len(s) - 1):
    first = s[i]
    second = s[i + 1]
    if abs(first) % 3 == 0 and abs(second) % 3 == 0:
        k += 1
        summ = first + second
        maxsumm = max(summ, maxsumm)
print(k, maxsumm)
