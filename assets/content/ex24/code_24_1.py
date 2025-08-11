s = open('file.txt').readline()
s = s.replace('A', ' ').replace('C', ' ')
print(max(len(i) for i in s.split()))