from pprint import pprint


def check_row(row_to_check: list):
    cut_row = row_to_check.copy()
    del cut_row[0]
    del cut_row[-1]

    zeros_straight = 0
    for place in cut_row:
        if place == 0:
            zeros_straight += 1
        else:
            zeros_straight = 0
        if zeros_straight >= 4:
            return True

    return False


with open("26-2.txt", encoding="utf8") as file:
    occupied_places_count, places_in_row = map(int, file.readline().strip().split())
    rows = {}

    for _ in range(occupied_places_count):
        storey_number, row_number, occupied_place_number = map(
            int, file.readline().strip().split()
        )
        if (storey_number, row_number) not in rows.keys():
            rows[(storey_number, row_number)] = [0] * places_in_row
            rows[(storey_number, row_number)][0] = 1
            rows[(storey_number, row_number)][-1] = 1
        rows[(storey_number, row_number)][occupied_place_number - 1] = 1

suitable_rows = []
for key, value in rows.items():
    if check_row(value):
        suitable_rows.append(key[1])

best_row = max(suitable_rows)
print(best_row, len(suitable_rows))
# pprint(rows)
# pprint(suitable_rows)
