f = open('k7-m1.txt')
a = f.readline()
rang = 0
maxx = 0


for i in range(len(a)):
    if a[i] == 'C':
        rang = rang + 1
        if rang > maxx: 
            maxx = rang
    else: rang = 0


print(maxx) 