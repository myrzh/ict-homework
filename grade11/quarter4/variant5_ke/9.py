with open("tasks/9.txt", encoding="utf8") as f:
    seqs = []
    for line in f.readlines():
        temp_seq = [int(i) for i in line.strip().split()]
        seqs.append(temp_seq)


for seq in seqs:
    temp_seq = seq.copy()
    if sorted(temp_seq)[3] < sum(sorted(temp_seq)[:3]):
        pass
