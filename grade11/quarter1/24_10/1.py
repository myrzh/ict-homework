from itertools import permutations


def func(n_input):
    possible_nums = list(filter(lambda x: x[0] != 0, permutations([int(i) for i in str(n_input)], 2)))
    max_num = max(possible_nums, key=lambda x: int(str(x[0]) + str(x[1])))
    min_num = min(possible_nums, key=lambda x: int(str(x[0]) + str(x[1])))
    return int(str(max_num[0]) + str(max_num[1])) - int(str(min_num[0]) + str(min_num[1]))


count = 0
for i in range(800, 901):
    if func(i) == 30:
        count += 1

print(count)