str1 = input().split()
kol = int(str1[0])
sum_fake = int(str1[1])
sum_real = 0
bad = []
n = 0
while kol !=0:
    n = n +1
    str1 = input().split()
    chs1 = int(str1[0])
    chs2 = int(str1[1][1:])
    chs3 = int(str1[2][1:])
    punkt = chs1 * chs2
    sum_real = sum_real + punkt
    if punkt != chs3:
        bad.append(n)
    kol = kol - 1
if sum_fake == sum_real:
    print('0')
else:print(abs(sum_fake - sum_real))
print( *bad)
