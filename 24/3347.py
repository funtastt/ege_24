s = open('24.txt').readline()

k, m = 1, 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        k += 1
    else:
        k = 1
    m = max(m, k)

print(m)