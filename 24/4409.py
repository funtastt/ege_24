s = open('../24.txt').readline()

counts = {'C': 0, 'D': 0, 'E': 0}

for i in range(len(s) - 4):
    if s[i] == s[i+4] == 'C' and s[i+1] == s[i+3] == 'B' and s[i+2] in counts:
        counts[s[i+2]] += 1

print(counts)
print(sum(counts.values()))