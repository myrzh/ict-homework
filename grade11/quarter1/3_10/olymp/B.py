n, vadim_cash = input().split()
vadim_rubles, vadim_kopeks = map(int, vadim_cash.split(','))
there_are_chips = False
suitable_chips = []

for i in range(int(n)):
    chips_name, chips_cost = input().split()
    chips_rubles, chips_kopeks = map(int, chips_cost.split(','))
    if vadim_rubles >= chips_rubles and vadim_kopeks >= chips_kopeks:
        suitable_chips.append((chips_name, chips_rubles, chips_kopeks))

if suitable_chips:
    # print(suitable_chips)
    best_chips = max(suitable_chips, key=lambda x: x[1] + float('00.' + str(x[2])))
    print(best_chips[0])
else:
    print(-1)