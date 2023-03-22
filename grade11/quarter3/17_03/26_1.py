with open("26-k5.txt", encoding="utf8") as f:
    n_phones, n_cheap, n_premium = map(int, f.readline().strip().split())
    prices = []
    for _ in range(n_phones):
        line = f.readline().strip()
        prices.append(int(line))

prices.sort()
premium = prices[-n_premium:]
middle = prices[n_cheap:-n_premium]
print(sum(middle) / len(middle))
print(premium[0])
