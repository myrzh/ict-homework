s = '1' + '57' * 30
while '157' in s or '1' in s:
    if '157' in 's':
        s = s.replace('157', '5757571')
    else:
        if '1' in s:
            s = s.replace('1', '57')

print(s)
print(s.count('7'))