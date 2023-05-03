from itertools import product


count = 0
for word_tuple in product("АРБУЗ", repeat=6):
    word = "".join(word_tuple)
    if (word.count("А") == 3) and ("АА" in word) and ("ААА" not in word):
        count += 1

print(count)
