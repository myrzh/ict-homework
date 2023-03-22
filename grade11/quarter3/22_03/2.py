def func1(x, y, z, w):
    return (w <= y) == (x and z)


def func2(x, y, z, w):
    return (not x) or (not y) or (not z) or w


def func3(x, y, z, w):
    return (z or w) and (y and x)


print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = func1(x, y, z, w)
                f2 = func2(x, y, z, w)
                f3 = func3(x, y, z, w)
                f = f3
                if f:
                    print(x, y, z, w, int(f))
