def task_4(codes: list, condition_reversed=False):
    codes = [str(abs(i)) for i in codes]
    stop_codes = set()
    start_num = '0'

    if condition_reversed:
        for code in codes:
            for i in range(0, len(code) + 1):
                if code[i:len(code) + 1]:
                    stop_codes.add(code[i:len(code) + 1])
    else:
        for code in codes:
            for i in range(0, len(code) + 1):
                if code[0:i]:
                    stop_codes.add(code[0:i])
    
    while True:
        if start_num not in stop_codes:
            return start_num
        start_num = bin(int(start_num, 2) + 1)[2:]


answer = task_4([10, 111, 101], condition_reversed=True)