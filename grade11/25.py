def dividers(num):
    divs_set = set()
    for i in range(1, int(num ** 0.5 + 1)):
        if num % i == 0:
            divs_set.add(i)
            divs_set.add(num // i)
    return len(divs_set)


arr = [f'1{a}80{b}{c}{d}{e}{f}{g}' for a in range(0, 9)
       for b in list(range(0, 9)) + [''] for c in list(range(0, 9)) + ['']
       for d in list(range(0, 9)) + [''] for e in list(range(0, 9)) + ['']
       for f in list(range(0, 9)) + [''] for g in list(range(0, 9)) + ['']
       if dividers(int(f'1{a}80{b}{c}{d}{e}{f}{g}')) % 2 == 1]

print(arr)