def get_combinations():
    combs = []
    for a in range(1, 4):
        for b in range(1, 4):
            for c in range(1, 4):
                for d in range(1, 4):
                    for e in range(1, 4):
                        for f in range(1, 4):
                            for g in range(1, 4):
                                for h in range(1, 4):
                                    for i in range(1, 4):
                                        for j in range(1, 4):
                                            for k in range(1, 4):
                                                for l in range(1, 4):
                                                    for m in range(1, 4):
                                                        combs.append(
                                                            (
                                                                a,
                                                                b,
                                                                c,
                                                                d,
                                                                e,
                                                                f,
                                                                g,
                                                                h,
                                                                i,
                                                                j,
                                                                k,
                                                                l,
                                                                m,
                                                            )
                                                        )
    return combs
