line = open('24.txt').readline()

words = line.split('.')

m = 0
for i in range(2, len(words)):
    m = max(m, len(words[i-2]) + len(words[i-1]) + len(words[i]))

print(m + 2)