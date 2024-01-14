line = open('24.txt').readline()

k, m = 0, 0
start = ''

for i in range(0, len(line)):
    if line[i] == 'F':
        if k == 0:
            if line[i-1] in '0123456789':
                start = line[i-1]
            else:
                continue
        k += 1
    else:
        if k > 0:
            end = line[i]
            if start == end and int(start) % 2 == 1:
                m = max(m, k)
        k = 0
print(m)