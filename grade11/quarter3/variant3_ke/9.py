sixlets = []
with open("tasks/9.txt", encoding="utf8") as f:
    for line in f.readlines():
        sixlets.append([int(i) for i in line.strip().split()])

count = 0
for sixlet in sixlets:
    if len(set(sixlet)) == 5:
        good_div = False
        for numb1 in sixlet:
            sixlet_5 = sixlet.copy()
            del sixlet_5[sixlet_5.index(numb1)]
            for numb2 in sixlet_5:
                sixlet_4 = sixlet_5.copy()
                del sixlet_4[sixlet_4.index(numb2)]
                for numb3 in sixlet_4:
                    sixlet_3 = sixlet_4.copy()
                    del sixlet_3[sixlet_3.index(numb3)]
                    if numb1 + numb2 + numb3 == sum(sixlet_3):
                        # print(sixlet, numb1, numb2, numb3, sixlet_3)
                        good_div = True
        if good_div:
            count += 1

print(count)
