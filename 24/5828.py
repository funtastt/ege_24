line = open('24.txt').readline()

m = 0
for n in range(1, 10**6):
    l = len(str(n))

    if sum(int(k)**l for k in str(n)) == n:
        m = n

print(line.count(str(m)))