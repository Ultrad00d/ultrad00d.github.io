m = []
for n in range(1000):
    n2 = bin(n)[2:]
    if n2.count('1') % 2 == 0:
        n2 = '101' + n2[3:] + '01'
    else:
        n2 = '111' + n2[3:] + '10'
    if int(n2, 2) < 385:
        m.append(n)
print(max(m))