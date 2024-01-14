line = open('../24.txt').readline()

s = ''
m = 0

for ch in line:
    if ch in '0123456789':
        s += ch
    elif s:
        if int(s) % 2 == 1:
            m = max(m, int(s))
        s = ''
print(m)