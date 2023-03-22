k = 0
k_max = 0
f = open("tasks/24(23).txt")
s = f.readline()
s = s.replace("XY", "K")
s = s.replace("ZY", "B")
for i in s:
    if i in ("K", "B"):
        k_max = max(k, k_max)
        k += 1
    else:
        k = 0

print(k_max)
