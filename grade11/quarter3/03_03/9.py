from sys import stdin
from pprint import pprint


seqs = []
for line in stdin:
    seq = line.strip().split()
    seqs.append(tuple(int(i) for i in seq))

count = 0
for seq in seqs:
    if len(set(seq)) == 5:
        pass