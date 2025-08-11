from itertools import *

s = '345 467 14 123567 147 24 245'.split()
v = 'GA GF GE GD GC GB AF FE ED CD BC'.split()
print(*range(1,8))
for p in permutations('ABCDEFG',r=7):
    if all(str(p.index(b) + 1) in s[p.index(a)] for a, b in v):
        print(*p)
# 1 2 3 4 5 6 7
# C F B G D A E
# F C A G E B D
# Ответ: 57