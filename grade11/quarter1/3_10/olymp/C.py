VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
_ = input()

mistakes_count = 0
for word in input().split():
    mistake_1 = 0
    mistake_2 = 0
    even_odd_numb = 0
    for i in word:
        if i in VOWELS:
            mistake_2 += 1
            if even_odd_numb % 2 == 0:
                mistake_1 += 1
        elif even_odd_numb % 2 == 1:
                mistake_1 += 1
        even_odd_numb += 1
    mistakes_count += min(mistake_1, len(word) - mistake_1, len(word) - mistake_2)
print(mistakes_count)