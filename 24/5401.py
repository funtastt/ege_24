line=  open('24.txt').readline()

m = 0
words = line.split('A')[1:-1]

for i in range(0, len(words) - 3):
    if words[i] == words[i+1] == words[i+2]:
        k = len(words[i]) + len(words[i+1]) + len(words[i+2])
        m = max(m, k)

print(m + 4)