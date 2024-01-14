line = open('24.txt').readline()
k = 0
s = ''
for i in range(1, len(line)):
    prev, curr = line[i - 1], line[i]
    if prev < curr:
        s += curr
    else:
        if len(s) == 5:
            k += 1
        s = curr
print(k)
