lines = open('24.txt').readlines()

lines = [l for l in lines if l.count('R') < 30]

k, m = 0, 0

for line in lines:
    for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        indices = [i for i in range(0, len(line)) if line[i] == ch]
        for i in range(1, len(indices)):
            r = indices[i] - indices[i-1] + 1
            if r > 2:
                k += 1
                m = max(m, r)

print(m, k)