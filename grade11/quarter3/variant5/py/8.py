count = 0
for i in range(1000, 10000):
    s = str(i)
    if len(set(s)) == 3:
        if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
            count += 1
print(count)
