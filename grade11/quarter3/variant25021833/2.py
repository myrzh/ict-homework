def func(x, y, z, w):
    return ((x <= w) and ((not y) <= z)) <= ((z == x) or (w and (not y)))


print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = func(x, y, z, w)
                if not f:
                    print(x, y, z, w, int(f))
