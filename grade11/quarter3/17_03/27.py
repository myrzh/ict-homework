f = open("27-B.txt")
f = f.readlines()[1:]
a = []
e = []
for element in f:
    element = element.replace("\n", "").split()
    for f in element:
        e.append(int(f))
    a.append(e)
    e = []

middle = []
mini = []
dif3 = []
maxx = []
for j in a:
    dif3.append((sum(j) - max(j) - min(j)) - min(j))
    maxx.append(max(j))
    middle.append(sum(j) - max(j) - min(j))
    mini.append(min(j))
summ = sum(maxx)

c = 0
if summ % 2 != 0:
    c = 1
if summ % 2 == 0:
    c = 2
summa = sum(middle)
minimalism = 10000000
for p in dif3:
    if p < minimalism and p % 2 != 0:
        minimalism = p
if summa % 2 == 0 and c == 1:
    summarism = sum(mini)
elif summa % 2 != 0 and c == 2:
    summarism = sum(mini)
else:
    summarism = sum(mini) + minimalism
print(summarism)
