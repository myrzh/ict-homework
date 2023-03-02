# s = "hhhzz"
# s = s.replace("h", "F", 1)
# print(s)

s = "4" * 84
while "11111" in s or "444" in s:
    if "11111" in s:
        s = s.replace("11111", "44", 1)
    else:
        s = s.replace("444", "1", 1)

print(s)

# my_list = [1, 4, 8, 8, -2]
# my_list.sort()
# print(my_list)
