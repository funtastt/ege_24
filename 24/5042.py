line = open('24.txt').readline()

arr = [0] * len(line)
m = 0
for i in range(2, len(line)):
    if line[i-2] == line[i] and line[i] in 'XY':
        arr[i] = 1 + arr[i-3]
        m = max(m, arr[i])

print(m)