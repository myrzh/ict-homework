n = int(input())
a = []
cnt = 0
for i in range(n):
    a.append(int(input()))
for i in a:
    if i == 0:
        cnt += 1
if cnt != 0:
    print('YES')
else:
    print('NO')