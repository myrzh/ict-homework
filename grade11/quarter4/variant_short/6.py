from pprint import pprint


def func(x: int, A: list) -> bool:
    P = list(range(6, 45 + 1))
    Q = list(range(18, 52 + 1))
    return ((x in Q) == (x in P)) or (((x in P) and (x not in Q)) <= (x in A))


suitable_cuts = []
for i in range(0, 100):
    for j in range(i + 1, 100 + 1):
        A = list(range(i, j + 1))
        if all(func(x, A) for x in range(0, 100 + 1)):
            suitable_cuts.append(A)


pprint(sorted(suitable_cuts))
print()
min_cut = min(suitable_cuts, key=len)
print(min_cut)
print(len(min_cut) - 1)
