numb_10 = 49**10 + 7**30 - 49

numb_7 = ""
while numb_10 > 0:
    digit = numb_10 % 7
    numb_7 += str(digit)
    numb_10 = numb_10 // 7

print(numb_7[::-1].count("6"))


# n = "000000128372183000"
# n = n.strip("0")
# print(n)
