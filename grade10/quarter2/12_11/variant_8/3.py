from random import randint


prev_num = array[0]
pairs_count = 0
prev_max = -9999

array = [randint(-100, 100) for i in range(100)]

for i in array[1:]:
    act_num = i
    if act_num % 2 == 0 or prev_num % 2 == 0:
        pairs_count += 1
        pair_sum = act_num + prev_num
        if pair_sum > prev_max:
            prev_max = pair_sum

print(pairs_count)
print(prev_max)