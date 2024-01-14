line = open('24.txt').readline()

nums = line.split('ZZ')
m = 0

from fnmatch import fnmatch

for n in nums:
    if len(n) == 11 and all(k in '0123456789' for k in n):
        if fnmatch(n, '8???54???22'):
            m = max(m, int(n))

mult = 1
for k in str(m):
    if int(k) % 2 == 1:
        mult *= int(k)

print(mult)