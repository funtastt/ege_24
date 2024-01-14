line = open('24.txt').readline()

k = m = 5

for i in range(len(line) - 6):
    if line[i:i+3] == line[i+3:i+6]:
        k = 5
    else:
        k += 1
    m = max(m, k)
print(m)