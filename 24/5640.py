line = open('24.txt').readline()

nums = line.split('FF')
m = 0

for n in nums:
    if len(n) == 10:
        if n[0] + n[1] + n[4] + n[5] + n[9] == '44783':
            m = max(m, int(n))

print(sum(int(k) for k in str(m) if int(k) % 2 == 0))