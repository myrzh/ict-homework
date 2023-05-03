with open("tasks/26.txt", encoding="utf8") as f:
    students_count, places = map(int, f.readline().strip().split())

    students = []
    for _ in range(students_count):
        line = f.readline().strip().split()
        temp_arr = list(map(int, line))
        if len(temp_arr) == 5:
            temp_arr = temp_arr[:3] + [max(temp_arr[3], temp_arr[4])]
        temp_arr = [temp_arr[0]] + [sum(temp_arr[1:])]
        students.append(temp_arr)

only_1 = list(map(lambda x: x[1], filter(lambda x: x[0] == 1, students)))
students = list(map(lambda x: x[1], students))
only_1.sort(reverse=True)
students.sort(reverse=True)
# print(*only_1, sep="\n")
# print(*students, sep="\n")
print(only_1[places - 1], students[places - 1])
