s = open('file.txt')
s = s.replace('KEGE', 'KEG EGE')
print(max(len(i) for i in s.split()))