lines = [w for w in open('24.txt').readlines() if w.count('E') < 20]

m = 0
for line in lines:
    for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        m = max(m, line.rfind(ch) - line.find(ch))

print(m)