line = open('../24.txt').readline()

m = 0
s = ''
i = 0

while i < len(line) - 2:
    if line[i:i + 3] == 'ATG' and not s:
        s = 'ATG'
        i += 3
    elif line[i:i + 3] == 'TGA' or line[i:i + 3] == 'TAG':
        s = ''
        i += 1
    elif line[i:i + 3] == 'TAA':
        m = max(m, len(s) + 3)
        s = ''
        i += 1
    elif s:
        s += s[i]
        i += 1
    else:
        i += 1
print(m)
