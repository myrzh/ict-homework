n = 5**2019 - 5**1019 + 25**600 - 125
n5 = ""
while n > 0:
    n5 += str(n % 5)
    n //= 5

print(n5.count("4"))
