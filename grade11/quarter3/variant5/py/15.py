for a in range(0, 1000):
    fail = False

    def func(a_internal):
        global fail
        for x in range(0, 1000):
            for y in range(0, 1000):
                f = (x >= a_internal) or (y >= a_internal) or (x * y <= 270)
                if not f:
                    fail = True
                    return

    func(a)
    if not fail:
        print(a)
