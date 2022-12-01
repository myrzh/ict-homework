from functools import lru_cache
import sys


@lru_cache
def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return (2 * n - 1) * f(n - 1)

print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)
print(f(3516) / f(3513))