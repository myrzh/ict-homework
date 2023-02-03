def func(x, y, z, w):
    exp1 = (z <= w)
    exp2 = (y <= (not exp1))
    return (not exp2) and ((not z) <= ((not w) == x))


print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = func(x, y, x, w)
                if f:
                    print(x, y, z, w, int(f))
