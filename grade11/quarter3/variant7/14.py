def get_numb(x):
    return (
        2 * 17**4
        + 6 * 17**3
        + x * 17**2
        + 3 * 17**1
        + 4 * 17**0
        + 3 * 17**4
        + x * 17**3
        + 5 * 17**2
        + 9 * 17**1
        + 7 * 17**0
    )


for x in range(0, 17):
    if get_numb(x) % 13 == 0:
        print(get_numb(x) / 13)
        break
