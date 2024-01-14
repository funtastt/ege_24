line = open('24.txt').readline()

chars = []

for i in range(2, len(line)):
    if line[i-2] == line[i-1]:
        chars.append(line[i])

from collections import Counter

counter = Counter(chars)

print(counter.most_common()[0])