line = open('24.txt').readline()

words = line.split('.')

m = 0
for i in range(1, len(words)):
    m = max(m, len(words[i-1]) + len(words[i]))

print(m + 1)