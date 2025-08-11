from itertools import *

counter = 0
# переберем цифры 0-6 (число семеричное) repeat=5 раз
for p in product('0123456', repeat=5):
    # для проверки на соседние символы, удобнее
    # перестановку представить в виде строки: p = '10000'
    p = ''.join(p)

    # если это число, то его ведущий разряд не ноль
    if p[0] != '0':
        # если одна 6 и нет парных чисел
        if p.count('6') == 1  \
            and '00' not in p \
            and '11' not in p \
            and '22' not in p \
            and '33' not in p \
            and '44' not in p \
            and '55' not in p \
            and '66' not in p: counter += 1
print(counter)