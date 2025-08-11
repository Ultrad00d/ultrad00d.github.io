from functools import *

# Мы не будем создавать кэш f(n), тк ее значение
# не зависит от значений f(n), только от g(n).
def f(n):
    return 2 * (g(n - 3) + 8)

@lru_cache(None)
def g(n):
    if n < 10: return 2 * n
    return g(n - 2) + 1

# значение g(n) зависит от предыдущего значения
for n in range(16000): g(n)

print(f(15548))