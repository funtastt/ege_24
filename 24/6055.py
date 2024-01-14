words = open('24.txt').readline().split('F')[1:-1]

k, m = 0, 0

for w in words:
    if w.count('E') < 5:
        continue
    if all(sub_s.count('A') == 1 for sub_s in w.split('E')[1:-1]):
        m = max(m, k)


print(m + 2)
