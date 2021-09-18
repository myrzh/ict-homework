k = int(input())
m = int(input()) * 2
n = int(input())

parties = n // k
last_partia = n % k

if n <= k:
    print(m)
else:
    if last_partia != 0:
        print(parties * m + m)
    else:
        print(parties)

### NOT DONE