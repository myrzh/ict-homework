def numb_sum(n):
    summ = 0
    while n > 0:
        digit = n % 10
        summ += digit
        n //= 10
    return summ

def numb_reverse(n):
    reversed_numb = ''
    while n > 0:
        reversed_numb += n % 10
        n //= 10
    return int(reversed_numb)

def numb_min(n):
    min_numb = 700000
    while n > 0:
        digit = n % 10
        if digit < min_numb:
            min_numb = digit
        n //= 10
    return min_numb

count = 0
all_sum = 0

for i in range(2020, 647038 + 1):
    reversed_numb = numb_reverse(i)
    n0 = reversed_numb % 10
    reversed_numb //= 10
    n1 = reversed_numb % 10
    reversed_numb //= 10
    n2 = reversed_numb % 10

    if numb_sum(i) < 10 and numb_min(i) != n0 and numb_min(i) != n1 and numb_min(i) != n2:
        count += 1
        all_sum += i

arith_mean = all_sum / count
min_dist = 700000
min_dist_numb = 0

for i in range(2020, 647038 + 1):
    reversed_numb = numb_reverse(i)
    n0 = reversed_numb % 10
    reversed_numb //= 10
    n1 = reversed_numb % 10
    reversed_numb //= 10
    n2 = reversed_numb % 10
    
    if numb_sum(i) < 10 and numb_min(i) != n0 and numb_min(i) != n1 and numb_min(i) != n2:
        if abs(i - arith_mean) < min_dist:
            min_dist = abs(i - arith_mean)
            min_dist_numb = i

print(count, min_dist_numb)