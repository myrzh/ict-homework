from sys import exit
a = int(input())
if a == 1:
    print(1)
    exit()
    
n = 0
s = 0
for i in range(2, int(a ** 0.5) + 1):
    b = a / i
    if b == int(b):
        if b == i:
            s = s + 1
        n = n + 1
print((n * 2) - s + 2)