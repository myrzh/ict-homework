f = open('k7-45.txt')
array = f.readlines()[0]
array += 'A'

max_len = 0
prev = array[0]
len_s = []
for i in array[1:]:
    if i == prev == 'C':
        max_len += 1
    else:
        len_s.append(max_len)
        max_len = 1
    prev = i

print(max(len_s))