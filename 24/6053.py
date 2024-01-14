line = open('24.txt').readline()

words = line.split('O')[1:-1]

print(max(len(w)  for w in words if w.count('F') <= 2) + 2)