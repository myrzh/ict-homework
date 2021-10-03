a, b = map(int, input().split())
simme_90 = []
for i in range(a, b + 1):
    num_sum = 0
    num_list = [int(j) for j in str(i)]
    for k in num_list:
        num_sum += k ** len(str(i))
    if num_sum == i:
        simme_90.append(i)

try:
    magicjabka = simme_90[0]
except:
    print(-1)
else:
    print(*simme_90)