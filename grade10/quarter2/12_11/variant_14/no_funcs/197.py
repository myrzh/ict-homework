import os


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '17-10.txt')
with open(filename , 'r') as f:
    array = f.readlines()
for i in range(0, len(array)):
    array[i] = array[i].rstrip()
    
prev_num = array[0]
pairs_count = 0
prev_min = 21000

for i in array[1:]:
    act_num = i
    pair_sum = act_num + prev_num

    if len(str(pair_sum)):
        if int(str(pair_sum)[2]) > int(str(pair_sum)[1]):
            pairs_count += 1
            if pair_sum < prev_min:
                prev_min = pair_sum
    prev_num = i

print(pairs_count, prev_min)