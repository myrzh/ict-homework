f = open('k7-m4.txt')
a = f.readline()
rang = 0
maxx = 0
x = 1
sp = 0

for i in range (len(a)-1,0,-1):
    if a[i] == 'C':
        rang = rang + 1
        if rang >= 6: 
            sp = 1 
    else: 
        if sp == 1:          
            print (x, rang, "c" * (rang - 1) + "C")
            x = x + 1
            sp = 0
        rang = 0