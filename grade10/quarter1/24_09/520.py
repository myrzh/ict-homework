n = int(input())
n1 = n // 144
m = n % 144
n2 = m // 12
n3 = m % 12
if n3 * 105 > 1025:
    n2 = n2 + 1
    n3 = 0 
if n2 * 1025 + n3 * 105 > 11400:
    n1 = n1 + 1
    n2 = 0
    n3 = 0
print (n1, n2, n3)