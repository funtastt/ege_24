line = open('24.txt').readline()

line = line.replace('PR', 'P.R')
line = line.replace('RP', 'R.P')

words = line.split('.')
print(max(len(w) for w in words))