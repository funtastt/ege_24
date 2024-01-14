lines = open('24.txt').readlines()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
m = 0
s = lines[0]

for line in lines:
    k = 0

    for i in range(0, len(line) - 2):
        if line[i:i+2] in alphabet:
            k += 1
    if k != 0:
        if k >= m:
            m = k
            s = line
from collections import Counter
counter = Counter(s)
print(sum(l.count('B') for l in lines))