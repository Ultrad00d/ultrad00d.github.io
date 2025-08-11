s = open('file.txt').readline()
s = s.replace('B', ' ').replace('E', ' ')
print(max(len(i) for i in s.split()))