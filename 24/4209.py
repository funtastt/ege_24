line = open('24.txt').readline()

words = line.split('KEGE')

m = 0

for i in range(0, len(words) - 2):
    k = len(words[i]) + len(words[i+1]) + len(words[i+2])
    m = max(m, k)

print(m + 14)