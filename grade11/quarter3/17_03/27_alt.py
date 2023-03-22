file = open("27-B.txt")
lines = file.readlines()[1:]
triples = []
for line in lines:
    element = line.strip().split()
    element = tuple(map(int, element))
    triples.append(element)
file.close()

mins = []
middles = []
maxs = []
diffs = []
for triple in triples:
    diffs.append((sum(triple) - max(triple) - min(triple)) - min(triple))
    maxs.append(max(triple))
    middles.append(sum(triple) - max(triple) - min(triple))
    mins.append(min(triple))
maxs_sum = sum(maxs)

even_condition = "default"
if maxs_sum % 2 != 0:
    even_condition = "odd"
if maxs_sum % 2 == 0:
    even_condition = "even"
middles_sum = sum(middles)

odds = [i for i in diffs if i % 2 != 0]
min_odd = min(odds)

if middles_sum % 2 == 0 and even_condition == "odd":
    mins_sum = sum(mins)
elif middles_sum % 2 != 0 and even_condition == "even":
    mins_sum = sum(mins)
else:
    mins_sum = sum(mins) + min_odd
print(mins_sum)
