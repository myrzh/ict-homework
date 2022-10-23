number = int(input())
count = 1
while True:
    number_str = str(number)
    if number == 1:
        break
    if int('1' * len(number_str)) <= number < int('21' + '0' * (len(number_str) - 2)) \
        and len(number_str) > 1:
        break
    elif number < int('1' * len(number_str)):
        number -= int((len(number_str) - 1) * '1')
        count += 1
    else:
        number -= int(len(number_str) * '1')
        count += 1
print(count)