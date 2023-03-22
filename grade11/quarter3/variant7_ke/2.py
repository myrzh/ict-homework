def func(x, y, z, w):
    return ((x <= y) <= z) or (w <= (y and z))


for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                pass
