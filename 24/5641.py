line = open('24.txt').readline()

nums = line.split('CC')
m = 0

from fnmatch import fnmatch

for n in nums:
    if len(n) == 12 and all(k in '0123456789' for k in n):
        if fnmatch(n, '234???57???8'):
            m = max(m, int(n))

ans = 1
for k in str(m):
    if int(k) % 2 == 1:
        ans *= int(k)
print(ans)