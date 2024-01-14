line = open('../24.txt').readline()

digits = '0123456789'

m, k = 1, 1

for i in range(1, len(line)):
    prev, curr = line[i-1], line[i]
    if ((prev in digits) + (curr in digits)) == 1:
        curr += 1
    else:
        curr = 1
    m = max(m, k)
print(m)
