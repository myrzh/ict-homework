from itertools import product
from collections import Counter


ALPH = "QWERTYNO"
count = 0
for password in product(ALPH, repeat=7):
    if "QWERTY" in password:
        continue
    if not all(i == 1 for i in Counter(password).values()):
        continue
    count += 1

print(count)
