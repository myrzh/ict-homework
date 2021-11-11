count = 0
max_num = 0
bin_str = ''

for i in range(10, 9999 + 1):
    n = i
    
    while n > 0:
        bin_str = str(n % 2) + bin_str
        n = n // 2

    if bin_str[-1] == '1' and bin_str.count('0') == 5 and int(bin_str) % 3 == 0 and int(bin_str) % 11 == 0:
        count += 1
        if i > max_num:
            max_num = i
    
    bin_str = ''

print(count)
print(max_num)