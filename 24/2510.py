line = open('24.txt').readline()

while 'D' in line or 'E' in line:
    line = line.replace('D', '.').replace('E', '.')

words = line.split('.')

print(max([len(w) for w in words]))