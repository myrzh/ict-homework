from itertools import product


def verify_word(word: tuple):
    if word.count("О") == 1:
        o_index = word.index("О")
        if o_index == 0:
            if word[o_index + 1] not in "КФ":
                return True
        if o_index == 4:
            if word[o_index - 1] not in "КФ":
                return True
        if word[o_index - 1] not in "КФ" and word[o_index + 1] not in "КФ":
            return True
    return False


first_happened = False
for count, line in zip(range(1, 1025), product("ЕКОФ", repeat=5)):
    if verify_word(line):
        if not first_happened:
            first_happened = True
            first_suitable = (count, line)
        last_suitable = (count, line)

print(first_suitable)
print(last_suitable)
