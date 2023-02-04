line = input()
alones = "".join(sorted(list(filter(lambda x: line.count(x) == 1, line))))
if alones:
    print(alones)
else:
    print("NO")
