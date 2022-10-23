_, max_sights = map(int, input().split())
towns = list(map(int, input().split()))
for town_index, town_sights in enumerate(towns):
    distance_left = town_index
    distance_right = len(towns) - town_index - 1
    max_distance = max(distance_left, distance_right)
    if town_sights > max_sights:
        print(-1)
        continue

    temp_index = town_index + max_distance
    temp_list = [0] * max_distance
    temp_list.extend(towns)
    temp_list.extend([0] * max_distance)
    # print(temp_list)
    # print(towns[town_index])
    # print(temp_list[temp_index])
    # print()

    distance = town_sights
    steps_made = 0
    for i in range(1, max_distance + 1):
        if distance + temp_list[temp_index + 1] + temp_list[temp_index - 1] > max_sights:
            print(temp_list)
            print(steps_made)
            print('BREAKED')
            print()
            break
        else:
            distance += temp_list[temp_index + 1] + temp_list[temp_index - 1]
        steps_made += 1
    else:
        print(steps_made)
        print()