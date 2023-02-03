numb = 243 ** 540 - 6 * 9 ** 530 + 21 * 3 ** 511 - 3 * 3 ** 70 - 200
nine_numb = ''
while numb > 0:
    nine_numb += str(numb % 9)
    numb //= 9
# nine_numb = nine_numb[::-1]
# print(nine_numb)
print(nine_numb.count('8'))
