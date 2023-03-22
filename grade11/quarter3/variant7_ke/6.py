from math import sqrt


count = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        if x > 0 and x < 31 * sqrt(3):
            if y < sqrt(3) * x / 3 + 31 and y < -sqrt(3) * x / 3 + 62:
                if y > -sqrt(3) * x / 3 and y < sqrt(3) * x / 3 - 31:
                    count += 1
print(count)
