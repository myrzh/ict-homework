towns_number, max_sights = map(int, input().split())
towns = ['0'] + input().split() + ['0']
towns = [int(i) for i in towns]

for i in range(1, towns_number + 1):
    temp_max_sights = max_sights
    steps = -1
    if towns[i] > temp_max_sights:
        print(steps)
        continue
    else:
        steps += 1
        temp_max_sights -= int(towns[i])
    for j in range(1, max(towns_number - i, i - 1) + 1):
        distance = towns[(i - j + abs(i - j)) // 2] + towns[(i + j + towns_number + 1
                - abs(i + j - towns_number - 1)) // 2]
        if distance > temp_max_sights:
            break
        else:
            temp_max_sights -= distance
            steps += 1
    print(steps)
