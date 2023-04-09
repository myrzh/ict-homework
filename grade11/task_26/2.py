from pprint import pprint


with open("tasks/26-62.txt", encoding="utf8") as f:
    n_goods, max_money = map(int, f.readline().strip().split())
    q = []
    z = []
    for line in f.readlines():
        price, good_type = line.strip().split()
        match good_type:
            case "Q":
                q.append(int(price))
            case "Z":
                z.append(int(price))
q.sort()
z.sort()

used_money_only_z = 0
for index, item in enumerate(z):
    if used_money_only_z + item <= max_money:
        used_money_only_z += item
    else:
        max_index_only_z = index
        break

usable_z = z[:max_index_only_z]

# 80 35
combs = []
for q_index, q_item in enumerate(q):
    for z_index, z_item in enumerate(usable_z):
        new_q = q[:q_index]
        new_z = z[:q_index]
        full = new_q + new_z
        combs.append((len(full), sum(full), len(new_z)))

combs = list(filter(lambda x: x[1] <= max_money, combs))
combs.sort(key=lambda x: (x[0], max_money - x[1], -x[2]))
pprint(combs)
