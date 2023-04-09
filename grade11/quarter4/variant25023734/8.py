from itertools import product


n = 0
for line in product("АВЛОР", repeat=4):
    n += 1
    print(n, "".join(line))
    if "".join(line) == "ЛААА":
        break
