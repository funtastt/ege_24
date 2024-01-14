line = open('24.txt').readline()

k = m = 0
for i in range(len(line) - 4):
    if ((line[i] == 'D') + (line[i + 1] == 'A') + (line[i + 2] == 'N') + (line[i + 3] == 'O') + (line[i + 4] == 'V')) == 4:
        k = 1
    else:
        k += 1

    m = max(m, k)

print(m)