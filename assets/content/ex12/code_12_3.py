res = []
for n in range(3, 10_001):
    s = '4' + n * '1'
    while '411' in s or '1111' in s:
        s = s.replace('411', '14', 1)
        s = s.replace('1111', '1', 1)
    res.append(sum(map(int, s)))
print(max(res))