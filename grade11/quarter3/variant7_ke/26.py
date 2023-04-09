from pprint import pprint


def check_list(row_list: list) -> bool:
    for i in range(len(row_list) - 1):
        first = row_list[i]
        second = row_list[i + 1]
        if abs(first - second) == 4:
            return True
    return False


with open('tasks/26.txt', encoding='utf8') as f:
    n_pixels = int(f.readline().strip())
    pixels_list = [tuple(map(int, line.strip().split())) for line in f.readlines()]

pixels_dict_temp = {}
for row, column in pixels_list:
    if row in pixels_dict_temp.keys():
        pixels_dict_temp[row].append(column)
    else:
        pixels_dict_temp[row] = [column]

pixels_dict = {}
for row in pixels_dict_temp.keys():
    if len(pixels_dict_temp[row]) >= 2:
        if check_list(sorted(pixels_dict_temp[row])):
            pixels_dict[row] = sorted(pixels_dict_temp[row])

pprint(pixels_dict)
