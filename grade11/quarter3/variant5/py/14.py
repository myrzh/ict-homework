alph = "0123456789abcdefg"
for x in alph:
    numb1 = int(f"135{x}9", 17)
    numb2 = int(f"9{x}531", 17)
    numb3 = numb1 + numb2
    if numb3 % 9 == 0:
        print(x)
        print(numb3 / 9)
        print()
