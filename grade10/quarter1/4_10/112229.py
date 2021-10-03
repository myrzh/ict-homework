numb = int(input())
dividers = []

for i in range(numb - 1, 1, -1):
    if (numb % i == 0):
        dividers.append(i)

dividers.reverse()
dividers.insert(0, 1)

if sum(dividers) == numb:
    if numb == 28:
        print(' ', end='')
    print(*dividers)
else:
    print(0)
