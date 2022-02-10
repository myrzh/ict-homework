f = open('k7c-1.txt')
array = f.readlines()[0]

count = 0
for i in range(0, len(array) - 2):
    seq = array[i:i + 3]
    if seq[0] in ['B', 'С', 'D']:
        if seq[1] != seq[0] and seq[1] in ['B', 'D', 'E']:
            if seq[2] != seq[1] and seq[2] in ['B', 'С', 'E']:
                count += 1

print(count)