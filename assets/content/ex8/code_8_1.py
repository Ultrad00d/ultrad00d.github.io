from itertools import *

for p in product([0, 1], repeat=3):
    print(p)
# (0, 0, 0)
# (0, 0, 1)
# (0, 1, 0)
# (0, 1, 1)
# (1, 0, 0)
# (1, 0, 1)
# (1, 1, 0)
# (1, 1, 1)