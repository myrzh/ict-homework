a = 15
r = 2
length = 18 # вычислено методом подбора

array = [a * r ** (n - 1) for n in range(1, length + 1)]
valid_array = []
times_equal = 0

for i in array:
    numb_array = [j for j in str(i)]
    for x in numb_array:
        for y in str(i):
            if y == x:
                times_equal += 1
    if times_equal > len(str(i)):
        valid_array.append(i)
    times_equal = 0

print(len(valid_array), max(valid_array) - min(valid_array))