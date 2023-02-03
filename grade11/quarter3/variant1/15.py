def is_triangle(a, b, c):
    max_side = max(a, b, c)
    min_side = min(a, b, c)
    middle_side = a + b + c - max_side - min_side
    return max_side < min_side + middle_side


def max_modded(a, b):
    if a > b:
        return a
    elif a <= b:
        return b


for a in range(1, 1000):
    false_happened = False
    for x in range(1, 1000):
        if not((is_triangle(x, 11, 18) == (not(max_modded(x, 5) > 15))) or is_triangle(x, a, 5)):
            continue
        else:
            false_happened = True
            break
    print(a, false_happened)
