a = int(input())
print((a // 100) - ((a % 100) % 10 * 10 + (a % 100) // 10) + 1) # no idea how this works