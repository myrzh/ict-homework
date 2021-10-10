a = int(input())
b = int(input())
c = int(input())
d = int(input())
solutions = []

for x in range(0, 1000 + 1):
    if a * x ** 3 + b * x ** 2 + c * x + d == 0:
        solutions.append(x)

if len(solutions) != 0:
    print(*reversed(solutions))