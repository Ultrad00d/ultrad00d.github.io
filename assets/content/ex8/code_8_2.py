from itertools import *

for p in permutations('ABC', r=2):
    print(p)
# ('A', 'B')
# ('A', 'C')
# ('B', 'A')
# ('B', 'C')
# ('C', 'A')
# ('C', 'B')

for p in permutations('ABC', r=3):
    print(p)
# ('A', 'B', 'C')
# ('A', 'C', 'B')
# ('B', 'A', 'C')
# ('B', 'C', 'A')
# ('C', 'A', 'B')
# ('C', 'B', 'A')