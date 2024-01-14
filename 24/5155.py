line = open('24.txt').readline()

arr = [0] * len(line)
m = 0

for i in range(1, len(line)):
    if line[i-1:i+1] in {'AA', 'CC'}:
        arr[i] = 1 + arr[i-2]
        m = max(m, arr[i])

print(m)
