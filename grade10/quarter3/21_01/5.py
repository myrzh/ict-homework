f = open('k7c-6.txt')
array = f.readlines()[0]

count = 0
for i in range(0, len(array) - 2):
    seq = array[i:i + 3]
    if seq[0] != seq[1] != seq[2]:
        count += 1
    print(seq)

print(count)