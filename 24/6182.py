line = open('24.txt').readline()

v1 = max(len(w) for w in [w for w in line.replace('A', ' A').replace('D', 'D ').split() if w[0] == 'A' and w[-1] == 'D'])
v2 = max(len(w) for w in [w for w in line.replace('A', 'A ').replace('D', ' D').split() if w[0] == 'D' and w[-1] == 'A'])

print(max(v1, v2))