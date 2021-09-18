import random


array = [random.randint(1, 1000) for i in range(30)]
max_cargo = int(input())
cargo_weight = 0
for i in array:
    cargo_weight += i
print(cargo_weight)
if cargo_weight <= max_cargo:
    print('OK')
else:
    print('NOT OK')