from pprint import pprint


with open("tasks/26_1.txt", encoding="utf8") as f:
    max_len, n_requests = map(int, f.readline().strip().split())
    requests = []
    for _ in range(n_requests):
        requests.append(tuple(map(int, f.readline().strip().split())))

requests.sort(key=lambda x: (x[0], x[1]))
pprint(requests)
