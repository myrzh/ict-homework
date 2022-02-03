import os, sys


fin = open('17-10.txt')
lst = fin.readlines()

prev_num = 0
pairs_count = 0
prev_min = 21000
first_iter = True

for i in lst:
    n = int(i)
    
    if first_iter:
        prev_num = n
        first_iter = False
        continue

    act_num = n
    pair_sum = act_num + prev_num

    if len(str(pair_sum)):
        if int(str(pair_sum)[2]) > int(str(pair_sum)[1]):
            pairs_count += 1
            if pair_sum < prev_min:
                prev_min = pair_sum
    prev_num = n

print(pairs_count, prev_min)
fin.close()