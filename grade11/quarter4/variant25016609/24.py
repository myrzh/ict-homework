with open("tasks/24.txt", encoding="utf8") as f:
    s = f.readline().strip().replace("DD", "D D").split()

s = list(filter(lambda x: "FE" in x, s))
print(len(max(s, key=len)))
