with open("tasks/24.txt", encoding="utf8") as f:
    line = f.readline().strip()


line = line.replace("QQ", "Q Q")
line = line.replace("QR", "Q R")
line = line.replace("QS", "Q S")
line = line.replace("RQ", "R Q")
line = line.replace("RR", "R R")
line = line.replace("RS", "R S")
line = line.replace("SQ", "S Q")
line = line.replace("SR", "S R")
line = line.replace("SS", "S S")


lst = line.split()
lst = sorted(lst, key=len)
for i in lst:
    print(len(i), i)
# print(len(max(lst, key=len)))
