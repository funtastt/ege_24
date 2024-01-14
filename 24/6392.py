s = open('24.txt').readline()

k = m = 2

for i in range(2, len(s)):
    if (s[i-2] in 'NOT') and (s[i] in 'NOT'):
        k = 2
    else:
        k += 1
    m = max(m, k)
print(m)