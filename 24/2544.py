line = open('24.txt').readline()
k = 0

for i in range(len(line)):
    if line[i:i + 3] == 'OCK' and line[i - 2:i + 3] != 'STOCK':
        k += 1

print(k)
