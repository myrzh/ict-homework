array = []
with open("26.txt") as f:
    space, num_of_files = map(int, f.readline().strip().split())
    for line in f.readlines():
        array.append(int(line.strip()))

array.sort()

new_arr = []
for i in array:
    if sum(new_arr) + i > space:
        break
    new_arr.append(i)

print(len(array))
# print(*array, sep='\n')
# print(*new_arr, sep='\n')
print(len(new_arr))
# print(sum(new_arr))
print(max(new_arr))
