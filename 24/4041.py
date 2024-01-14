lines = open('24.txt').readlines()

lines = [l for l in lines if l.count('G') < 15]

m = 0

for line in lines:
    for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if line.count(ch) >= 2:
            m = max(m, line.rindex(ch) - line.index(ch))

print(m)