line = open('24.txt').readline()

s = ''
max_s = ''
ans = 0

for i in range(1, len(line)):
    if line[i-1] < line[i]:
        s += line[i]
    else:
        s = line[i]
    if len(s) > len(max_s):
        max_s = s
        ans = i - len(s) + 2

print(ans)