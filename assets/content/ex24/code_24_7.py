s = open('file.txt')
s = s.split('A')
m = 0
for i in range(len(s) - 1):
    c = s[i] + 'A' + s[i + 1] + 'A' + s[i + 2] + 'A' + s[i + 3]
    # если букв МНОГО
    # c = 'А'.join(s[i:i+4])
    m = max(m, len(c))
print(m)