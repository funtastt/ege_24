words = open('24.txt').readline().split('E')[1:-1]

m = 10**6

for w in words:
    if w.count('B') == 2:
        if w.split('B')[1].count('A') > 5:
            m = min(m, len(w))

print(m + 2)


