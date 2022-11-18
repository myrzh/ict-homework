f = open('27_A.txt')
a, b = map(int,f.readline().split())
ar = [(int(i.strip().split()[0]), int(i.strip().split()[1])) for i in f.readlines()]
pr = 0
g = 0
maxx = 0
print (ar)


while ar[g][0] < b:
    g = g + 1
s = g
while ar[s][0] < 2*b:
    s = s + 1     
l_border = 0
r_border = s
for i in range (l_border,r_border):
    maxx = maxx + ar[i][1]

for i in range (g,ar[a-1][0]):
    
    
    
    if  pmax > maxx:
        pr = i
        maxx = pmax