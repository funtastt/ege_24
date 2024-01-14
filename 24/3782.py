lines = open('24.txt').readlines()

s = lines[0]

for line in lines:
    if line.count('Q') < s.count('Q'):
        s = line

from collections import Counter

counter = Counter(s)
print(sum(l.count('C') for l in lines))