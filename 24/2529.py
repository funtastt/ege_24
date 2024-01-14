line = open('24.txt').readline()

s = ''
max_s = ''

for i in range(1, len(line)):
    if line[i-1] < line[i]:
        s += line[i]
    else:
        s = line[i]
    if len(s) > len(max_s):
       max_s = s
print(max_s, len(max_s))