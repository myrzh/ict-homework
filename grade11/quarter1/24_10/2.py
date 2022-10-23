from sys import exit


LETTERS = ['A', 'L', 'P', 'C', 'Y']

count = 1
for l1 in LETTERS:
    for l2 in LETTERS:
        for l3 in LETTERS:
            for l4 in LETTERS:
                for l5 in LETTERS:
                    word = l1 + l2 + l3 + l4 + l5
                    print(count, word)
                    count += 1
                    if word.count('A') <= 1 and word.count('C') == 2 and word.count('L') == 0:
                        exit()