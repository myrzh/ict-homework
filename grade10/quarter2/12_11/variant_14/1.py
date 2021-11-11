count = 0
max_num = 0
for i in range(1007, 746001 + 1):
    if str(i)[0] == str(max([int(j) for j in str(i)])):
        if str(i).count('5') >= 2 and str(i).count('5') % 2 == 0:
            count += 1
            if str(i)[0:2] == '50':
                if i > max_num:
                    max_num = i

print(count)
print(max_num)