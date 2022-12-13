out = open('24_out.txt', 'w')
with open('24.txt') as f:
    line = f.readline()
    print(type(line))
    for i in line:
        out.write(i)
        out.write('\n')