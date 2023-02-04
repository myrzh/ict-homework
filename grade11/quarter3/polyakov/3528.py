with open("24-153.txt", encoding="utf-8") as f:
    line = f.readline().strip()

    while "DD" in line:
        line = line.replace("DD", "D")
    line_list = line.split("D")

    print(len(min(line_list, key=len)) + 2)
