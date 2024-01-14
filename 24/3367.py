s = open('../24.txt').readline()

max_len = 0
curr = 1

for i in range(1, len(s)):
    if s[i-1] < s[i]:
        curr += 1
    else:
        curr = 1
    max_len = max(max_len, curr)

print(max_len)