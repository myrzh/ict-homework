from functools import lru_cache
from sys import setrecursionlimit


setrecursionlimit(18000)


@lru_cache
def f(n):
    if n == 1:
        return 3
    if n % 2 == 0:
        return f(n - 1) + 5 * (n - 1)
    return f(n - 1) + 7


print(f(8765))
print("asdasd")
