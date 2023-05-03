from pprint import pprint


def check_row(row: list) -> int:
    for index in range(len(row) - 1):
        first = row[index]
        second = row[index + 1]
        count = 0
        if second - first == 12:
            count += 1
        return count


places_dict = {}

with open("files/26.txt", encoding="utf8") as f:
    places_numb = int(f.readline().strip())
    for _ in range(places_numb):
        line_list = f.readline().strip().split()
        row, place = map(int, line_list)
        # print(row, place)
        if row not in places_dict.keys():
            places_dict[row] = [place]
        else:
            places_dict[row].append(place)

suitable_rows = []
for key, value in places_dict.items():
    good_places = check_row(sorted(value))
    if good_places > 0:
        suitable_rows.append((key, good_places))

summ = 0
for i in suitable_rows:
    summ += i[1]
print(max(suitable_rows, key=lambda x: x[0])[0], summ)
# pprint(suitable_rows)
