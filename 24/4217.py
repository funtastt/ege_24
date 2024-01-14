line = open('24.txt').readline()

line = line.replace('QW', 'Q.W')

words = line.split('.')

print(max([len(w) for w in words]))