line = open('24.txt').readline()

chars = []

for i in range(1, len(line) - 1):
    if line[i-1] == line[i+1]:
        chars.append(line[i])

from collections import Counter

counter = Counter(chars)

print(counter.most_common()[0])