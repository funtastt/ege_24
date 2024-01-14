line = open('24.txt').readline()

s = ''

while (s+'DAD') in line:
    s += 'DAD'

m = 0
for start in ('D', 'AD'):
    for end in ('D', 'DA'):
        new_s = start + s + end
        if new_s in s:
            m = max(m, len(new_s))