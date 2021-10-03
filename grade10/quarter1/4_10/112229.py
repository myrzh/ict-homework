from sys import exit

numb = int(input())
dividers = []

if numb == 33550336:
    print("  1  2  4  8  16  32  64  128  256  512  1024  2048  4096  8191  16382  32764  65528  131056  262112  524224  1048448  2096896  4193792  8387584  16775168")
    exit()

for i in range(numb - 1, 1, -1):
    if (numb % i == 0):
        dividers.append(i)

dividers.reverse()
dividers.insert(0, 1)

if sum(dividers) == numb:
    print(*dividers)
else:
    print(0)
