line = open('24.txt').readline()

arr = [0] * len(line)
m = 0
for i in range(2, len(line)):
    if line[i-2] in 'BCDF' and line[i-1] in 'BCDF' and line[i] in 'AEO':
        arr[i] = arr[i-3] + 1
        m = max(m, arr[i])

print(m)