f = open('k7a-6.txt')
array = f.readlines()[0]
array += 'E'
alph = ['B', 'C', 'D', 'F']

max_len = 0
len_s = []
for i in array:
    if i in alph:
        max_len += 1
    else:
        len_s.append(max_len)
        max_len = 1

print(max(len_s))

# TODO: THE TASK