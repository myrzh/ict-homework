with open("tasks/24.txt", encoding="utf8") as f:
    s = f.readline().strip()

max_list = []
count = 0
for i in range(len(s) - 1):
    if ord(s[i]) <= ord(s[i + 1]):
        count += 1
    else:
        max_list.append(count)
        count = 0

print(max(max_list) + 1)
