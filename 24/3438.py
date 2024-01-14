line = open('24.txt').readline()

k = 0
for i in range(0, len(line) - 5):
    s = line[i:i+5]
    if s == s[::-1]:
        k += 1
print(k)