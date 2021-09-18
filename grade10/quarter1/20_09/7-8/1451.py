a = int(input())
b = int(input())
c = int(input())
is_there_even = False
is_there_odd = False

if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    is_there_even = True
if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
    is_there_odd = True

if is_there_even == True and is_there_odd == True:
    print('YES')
else:
    print('NO')