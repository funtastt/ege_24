line = open('24.txt').readline()

nums = line.split('RR')
m = 0

from fnmatch import fnmatch

for n in nums:
    if len(n) == 12 and all(k in '0123456789' for k in n):
        if fnmatch(n, '322??55???89'):
            m = max(m, int(n))

mult, summ = 1, 0
for k in str(m):
    if int(k) % 2 == 1:
        mult *= int(k)
    else:
        summ += int(k)
print(mult+summ)