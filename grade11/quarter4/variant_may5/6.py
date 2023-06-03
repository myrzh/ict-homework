from math import sqrt


count = 0
for x in range(1000):
    for y in range(1000):
        if y < sqrt(3) * x and y > sqrt(3) * x - 15 * sqrt(3):
            if y < 15 * sqrt(3) and y > 0:
                count += 1

print(count)
