def func(x, y, z, w):
    return not(z or x) or y and (not x) and ((z and y) <= z)

print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = func(x, y, z, w)
                if f:
                    print(x, y, z, w, int(f))
