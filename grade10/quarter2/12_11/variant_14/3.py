from random import randint


array = [randint(0, 10000) for i in range(100)]

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

print(pairs_count)
print(prev_min)