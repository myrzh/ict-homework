def func(numb1, numb2):
    numb1 = str(numb1)
    numb2 = str(numb2)
    result = str(int(numb1[0]) + int(numb2[0]))
    result = result + str(int(numb1[1]) + int(numb2[1]))
    result = str(int(numb1[2]) + int(numb2[2])) + result
    return int(result[-4:-1])


for numb1 in range(100, 1000):
    for numb2 in range(100, 1000):
        res = func(numb1, numb2)
        print(numb1, numb2, res)
