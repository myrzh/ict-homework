def func(x, y, z, w):
    return (x and (not y)) or (y == z) or (not w)


print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = func(x, y, z, w)
                if not f:
                    print(x, y, z, w, int(f))
