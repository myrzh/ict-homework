count = 0
max_num = 0
bin_str = ''

for i in range(10, 9999 + 1):
    n = i
    zero_count = 0
    
    while n > 0:
        bin_str = str(n % 2) + bin_str
        n = n // 2
    
    for j in bin_str:
        if j == '0':
            zero_count += 1

    if bin_str[-1] == '1' and zero_count == 5 and i % 3 == 0 and i % 11 == 0:
        count += 1
        if i > max_num:
            max_num = i
    
    bin_str = ''

print(count, max_num)