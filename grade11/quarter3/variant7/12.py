def modify_line(s):
    while ">2" in s or ">3" in s or ">5" in s:
        if ">2" in s:
            s = s.replace(">2", "55>")
        if ">3" in s:
            s = s.replace(">3", "523>")
        if ">5" in s:
            s = s.replace(">5", "52>")
    return s


s = ">" + "2" * 12 + "3" * 22 + "5" * 15
new_s = modify_line(s)
digits_list = list(map(int, filter(lambda x: x.isdigit(), new_s)))
# print(digits_list)
print(sum(digits_list))
