a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
solutions = []

for x in range(0, 1000 + 1):
    try:
        if (a * x ** 3 + b * x ** 2 + c * x + d) / (x - e) == 0:
            solutions.append(x)
    except:
        pass

print(len(solutions))