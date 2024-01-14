line = open('24.txt').readline()

s = ''

m = 0

for ch in line:
    if ch == '0':
        if '1' not in s:
            s += ch
        else:
            m = max(m, len(s))
            s = '0'

    elif ch == '1' and s:
        s += ch
    else:
        if '0' in s and '1' in s:
            m = max(m, len(s))
        s = ''
print(m)