line = open('24.txt').readline()
k, m = 0, 0
for i in range(0, len(line) - 1):
    if line[i:i+2] in {'AB', 'CB','BC', 'BA'}:
        k += 1
    else:
        k = 0
    m = max(k, m)

print(m)