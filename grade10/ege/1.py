from itertools import product


numb = 1
def calc(command):
    global numb
    if command == 1: numb += 4
    if command == 2: numb -= 3


commands = product([1, 2], repeat=7)
results = set()

for i in commands:
    print(i)
    for j in i:
        calc(j)
    results.add(numb)
    numb = 1

print(len(results))