lines = open('24.txt').readlines()

s = lines[0]

for line in lines:
    if line.count('A') < s.count('A'):
        s = line

from collections import Counter

counter = Counter(s)
print(sum(l.count('V') for l in lines))