line = open('24.txt').readline()

line = line.replace('A', '.A').replace('B', 'B.')

words = line.split('.')
k = 0

for w in words:
    if len(w) >= 20 and w[0] == 'A' and w[-1] == 'B':
        k += 1

print(k)