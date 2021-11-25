def numb_reverse(n):
    reversed_numb = ''
    while n > 0:
        reversed_numb += str(n % 10)
        n //= 10
    return int(reversed_numb)

count = 0
prev_max = 0

for i in range(1007,746001 + 1):
    n = i
    digit = 0
    max_num = 0
    five_count = 0
    
    while n > 0:
        digit = n % 10
        if digit > max_num:
            max_num = digit
        if digit == 5:
            five_count += 1
        n //= 10
    
    n = numb_reverse(i)
    first_letter = n % 10
    n //= 10
    second_letter = n % 10

    if digit == max_num and five_count % 2 == 0 and five_count >= 2:
        count += 1
        if first_letter == 5 and second_letter == 0:
            if i > prev_max:
                prev_max = i

print(count, prev_max)
