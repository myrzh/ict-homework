"""
Введите битовую строку и дополните её последним битом, который должен быть равен 0,
если в исходной строке чётное число единиц, и равен 1, если нечётное
(в получившейся строке должно всегда быть чётное число единиц).
"""

a = input()
count = 0
for c in a:
    if c == '1':
        count += 1
if count % 2 == 0:
    a = a + '0'
else:
    a = a + '1'

print(a)