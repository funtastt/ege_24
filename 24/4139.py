line = open('24.txt').readline()

s = ''
while (s + 'XYZ') in line:
    s += 'XYZ'

print(len(s))