line = open('24.txt').readline()

chars = []

for i in range(0, len(line) - 1):
    if line[i] == 'A':
        chars.append(line[i+1])

from collections import Counter

counter = Counter(chars)

print(counter.most_common()[0])