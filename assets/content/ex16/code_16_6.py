from functools import *

@lru_cache(None)
def f(n):
    if n >= 3210: return 1
    return f(n + 3) + 7

@lru_cache(None)
def g(n):
    if n < 10: return n
    return g(n - 3) + 5

# значение f(n) зависит от следующего значения,
# поэтому перебираем n до нуля:
for n in range(3210, 0, -1): f(n)

# значение g(n) зависит от предыдущего значения,
# поэтому перебираем до n:
for n in range(3001): g(n)

print(f(15) - g(3000))