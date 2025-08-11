from functools import *

@lru_cache(None)
def f(n): ...

# если значение функции зависит от предыдущего:
for n in range(число):        f(n)
# если значение функции зависит от следующего:
for n in range(число, 0, -1): f(n)