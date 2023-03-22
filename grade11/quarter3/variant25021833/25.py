# 10000000000
# 01X2139XXX4

for ins0 in list(map(str, range(0, 10))):
    for ins1 in list(map(str, range(0, 10))) + [""]:
        for ins2 in list(map(str, range(0, 10))) + [""]:
            for ins3 in list(map(str, range(0, 10))) + [""]:
                numb_str = f"1{ins0}2139{ins1}{ins2}{ins3}4"
                numb_int = int(numb_str)
                if numb_int % 3052 == 0:
                    print(numb_str, numb_int // 3052)
