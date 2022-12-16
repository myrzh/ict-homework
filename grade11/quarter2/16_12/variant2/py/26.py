with open('26.txt') as f:
    reds_num, blues_num = map(int, f.readline().strip().split())
    reds = []
    blues = []
    for _ in range(blues_num):
        red_temp, blue_temp = map(int, f.readline().strip().split())
        reds.append(red_temp)
        blues.append(blue_temp)
    for _ in range(reds_num - blues_num):
        red_temp = int(f.readline().strip())

print(*blues, sep='\n')
print('\n' * 10)
print(*reds, sep='\n')