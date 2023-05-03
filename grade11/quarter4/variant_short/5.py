numb = 7 * 729**6 + 6 * 81**9 + 3**14 - 90
numb_9 = ""
while numb > 0:
    numb_9 += str(numb % 9)
    numb //= 9
numb_9 = numb_9[::-1].lstrip("0")
print(numb_9)
print(len(list(filter(lambda x: int(x) % 2 == 0, numb_9))))
