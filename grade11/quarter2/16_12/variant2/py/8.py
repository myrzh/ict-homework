import sys


alph = 'АЗЛОПЬ'
count = 0
for a in alph:
    for b in alph:
        for c in alph:
            for d in alph:
                for e in alph:
                    for f in alph:
                        word = a + b + c + d + e + f
                        count += 1
                        if word.count('Ь') <= 1 and word.count('А') == 1 and word.count('З') <= 2:
                            print(count)
                            sys.exit()