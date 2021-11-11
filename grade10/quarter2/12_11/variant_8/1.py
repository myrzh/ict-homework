count = 0
prev_max = 0

for i in range(9999, 99999 + 1):
    n = i
    summ = 0

    while n > 0:
        digit = n % 10
        summ = summ + digit
        n = n // 10
    
    if i % summ == 0:
        count += 1
        if i > prev_max:
            prev_max = i

print(count)
print(prev_max)