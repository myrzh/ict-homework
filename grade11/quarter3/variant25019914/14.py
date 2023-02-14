numb = 3 * 1024**75 + 2 * 256**76 - 16**77 - 2023
numb_32 = []
while numb > 0:
    numb_32.append(numb % 32)
    numb //= 32
numb_32 = numb_32[::-1]
print(numb_32.count(0))
print(numb_32)
