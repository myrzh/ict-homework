with open("tasks/24.txt", encoding="utf8") as f:
    line = f.readline().strip()


line = line.replace("A", "*")
line = line.replace("O", "*")
line = line.replace("C", "-")
line = line.replace("D", "-")
line = line.replace("F", "-")
line = line.replace("-*", "+")
line = line.replace("*", "/")
line = line.replace("-", "/")
line = line.split("/")

# print(max(line, key=len))
print(len(max(line, key=len)))
