line = open('24.txt').readline()

arr = [0] * len(line)
m = 0
digits = '0123456789'

for i in range(2, len(line)):
    if line[i-2] not in digits and line[i-1] in digits and line[i] in digits:
        arr[i] = arr[i-3] + 1
        m = max(m, arr[i])

print(m)