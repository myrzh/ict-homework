from pprint import pprint


with open("tasks/26-55.txt", encoding="utf8") as f:
    n_cargos, max_weight = map(int, f.readline().strip().split())
    cargos = list(map(lambda x: int(x.strip()), f.readlines()))

cargos.sort()
pprint(cargos)
last_sum = 0
n_sails = 0
for cargo in cargos:
    if last_sum + cargo <= max_weight:
        last_sum += cargo
    else:
        last_sum = cargo
        n_sails += 1

print(n_sails + 1, last_sum)
