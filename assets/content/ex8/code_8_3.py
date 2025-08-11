from itertools import *

for p in combinations('ABC', r=2):
    print(p)
# ('A', 'B')
# ('A', 'C')
# ('B', 'C')

for p in combinations('ABC', 3):
    print(p)
# ('A', 'B', 'C')
# нельзя составить еще одну тройку элементов
# в них всегда будет и 'A', и 'B', и 'C'