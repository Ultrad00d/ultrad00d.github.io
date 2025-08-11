s = open('file.txt')
s = s.replace('B', 'A').replace('C', 'A').replace('2', '1').replace('3', '1')
s = s.replace('A11', '*').replace('A', ' ').replace('1', ' ')
print(max(len(i) for i in s.split()))