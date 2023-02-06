# from itertools import combinations_with_replacement, combinations
# from pprint import pprint
from extra_23 import get_combinations


def chit(a):
    pr = [2]
    for i in range(0, len(a)):
        if a[i] == 1:
            pr.append(pr[i] + 2)
        if a[i] == 2:
            pr.append(pr[i] * 2)
        if a[i] == 3:
            pr.append(pr[i] * 3)
    return pr


iv = []
# programs = list((combinations_with_replacement('123', 14)))
programs = get_combinations()
for j in programs:
    tpr = chit(j)
    if 6 in tpr and 28 in tpr:
        iv.append(j[: tpr.index(28)])
        # print(j,end=" ")
        # print(tpr)

print(*set(iv), sep="\n")
print(len(set(iv)))
