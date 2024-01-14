s = open('../24.txt').readline()

counts = {'X': 0, 'Y': 0, 'Z': 0, 'W': 0, 'O': 0, 'P': 0}

for i in range(len(s) - 2):
    if s[i] == 'X' and s[i+2] == 'P' and s[i+1] in counts:
        counts[s[i+1]] += 1

print(max(counts.values()))