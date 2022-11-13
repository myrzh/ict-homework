number_of_farms, max_distance = map(int, input().split())
farms = []
for _ in range(number_of_farms):
    farms.append(tuple(int(i) for i in input().split()))

print(*farms, sep='\n')