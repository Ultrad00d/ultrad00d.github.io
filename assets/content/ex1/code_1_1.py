from itertools import *

s = '457 46 567 12 136 235 13'.split()   # у 1 связи с 457, у 2 с 46 и т.д.
v = 'FE EC CA AB BD DF FG DG GC'.split() # по графику есть связи FE, EC и т.д. 
print(*range(1, 8))
for p in permutations('ABCDEFG'):
    if all(str(p.index(b) + 1) in s[p.index(a)] for a, b in v):
        print(*p)