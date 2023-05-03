from itertools import product


count = 0
for word in product('НАСТЯ', repeat=7):
    line = ''.join(word)
    if line.count('Н') == 2 and line.count('А') >= 1:
        count += 1

print(count)
