strings = open('../24.txt').readline().replace('A', ' A').replace('B', 'B ').split()

count = 0

for s in strings:
    if s[0] == 'A' and s[-1] == 'B' and s.count('F') == 2 and len(s) >= 20:
        count += 1

print(count)