line = open('24.txt').readline()

line = line.replace('A', ' A').replace('F', 'F ')

words = [w for w in line.split() if w[0] == 'A' and w[-1] == 'F' and len(w) > 2]

print(min(len(w) for w in words))