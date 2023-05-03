from itertools import product


count = 0
for number in product("01234567", repeat=5):
    line = "".join(number)
    if line != line.lstrip("0"):
        continue
    # print(line)
    if line.count("6") == 1:
        flag = True
        for i in range(1, len(line) - 1):
            first = line[i - 1]
            second = line[i]
            third = line[i + 1]
            if second == "6" and (int(first) % 2 == 1 or int(third) % 2 == 1):
                flag = False
                break
        if (line[0] == "6" and int(line[1]) % 2 == 1) or (
            line[-1] == "6" and int(line[-2]) % 2 == 1
        ):
            flag = False
        if flag:
            count += 1

print(count)
