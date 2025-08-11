s = [int(k) for k in open('17_1.txt').readlines()]

# проход по двойкам
for i in range(len(s) - 2 + 1):
    a = [x for x in s[i:i + 2]]

# проход по тройкам
for i in range(len(s) - 3 + 1):
    a = [x for x in s[i:i + 3]]
    
# проход по группам из n элементов
for i in range(len(s) - n + 1):
    a = [x for x in s[i:i + n]]