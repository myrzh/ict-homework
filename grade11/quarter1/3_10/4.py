print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((not x) == z) <= (y == (w or x))
                if f == 0:
                    print(x, y, z, w)