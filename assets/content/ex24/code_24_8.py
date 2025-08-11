s = open('file.txt').readline()
m = [0]*len(s)

for i in range(1, len(s)):
    if s[i] in 'ACDF':
        m[i] = m[i - 1] + 1
print(max(m))