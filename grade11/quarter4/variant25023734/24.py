with open("tasks/24.txt", encoding="utf8") as f:
    line = f.readline().strip()

line = line.replace("Q", "*")
line = line.replace("R", "*")
line = line.replace("S", "*")

while "**" in line:
    line = line.replace("**", "* *")

line_list = line.split()
print(max(len(i) for i in line_list))
