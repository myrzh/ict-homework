def func(x, y, z, w):
    return (not(w <= (not(x <= y)))) and ((not z) <= ((not y) == z))

print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = func(x, y, z, w)
                if f:
                    print(x, y, z, w, 1)
