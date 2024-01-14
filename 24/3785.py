lines = open('24.txt').readlines()
m, k = 0, 1
s = lines[0]

for line in lines:
    for i in range(1, len(line)):
        prev, curr = line[i-1], line[i]
        if prev == curr:
            k += 1
        else:
            if k > m:
                s = line
                m = k
            k = 1
from collections import Counter
counter = Counter(s)
print(sum(l.count('Z') for l in lines))