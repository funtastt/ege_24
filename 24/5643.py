line = open('24.txt').readline()

nums = line.split('SS')[1:-1]
m = 0

from fnmatch import fnmatch

for n in nums:
    if len(n) == 11 and all(k in '0123456789' for k in n):
        if fnmatch(n, '12????77??9'):
            m = max(m, int(n))

mult, summ = 0, 1
for k in str(m):
    if int(k) % 2 == 1:
        mult += int(k)
    else:
        summ *= int(k)
print(mult+summ)