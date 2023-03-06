def modify_line(s):
    while ">1" in s or ">2" in s or ">*" in s:
        if ">1" in s:
            s = s.replace(">1", "111>", 1)
        if ">2" in s:
            s = s.replace(">2", "1>", 1)
        if ">*" in s:
            s = s.replace(">*", "%2*>", 1)
    return s


for k in range(100, 200 + 1):
    for m in range(100, 200 + 1):
        for n in range(100, 200 + 1):
            s = ">" + "1" * k + "2" * m + "*" * n
            new_s = modify_line(s)
            digits_list = list(map(int, filter(lambda x: x.isdigit(), new_s)))
            # print(digits_list)
            if sum(digits_list) == 1190:
                print(n)
                exit()
