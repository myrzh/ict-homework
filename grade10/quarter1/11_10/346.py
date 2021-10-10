n = int(input())
a = []
zero = 0
pos = 0
neg = 0
for i in range(n):
    a.append(int(input()))
for i in a:
    if i == 0:
        zero += 1
    if i > 0:
        pos += 1
    if i < 0:
        neg += 1

print(zero, pos, neg)