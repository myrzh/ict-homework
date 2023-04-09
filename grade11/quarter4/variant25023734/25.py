suitable_numbers = []

for r1 in range(0, 10):
    for r2 in range(0, 10):
        for r3 in list(range(0, 10)) + [""]:
            numb = int(f"12{r1}{r2}36{r3}1")
            if int(numb) % 273 == 0:
                suitable_numbers.append((numb, numb // 273))

suitable_numbers.sort(key=lambda x: x[0])
for i in suitable_numbers:
    print(i[0], i[1])
