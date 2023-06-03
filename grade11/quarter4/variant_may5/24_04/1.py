from pprint import pprint


with open("tasks/26_1.txt", encoding="utf8") as f:
    max_len, n_requests = map(int, f.readline().strip().split())
    requests = []
    for _ in range(n_requests):
        requests.append(tuple(map(int, f.readline().strip().split())))
requests.sort(key=lambda x: (x[1], x[0]))

good_requests = [requests[0]]
current_index = 1
for request in requests[1:]:
    if request[0] >= good_requests[current_index - 1][1]:
        good_requests.append(request)
        current_index += 1

print(len(good_requests), good_requests[-1][0])
pprint(requests)
