line = open('../24.txt').readline()

k, m = 0, 0

for ch in line:
    if ch in '0123456789ABCDEF':
        if k > 0 or ch != '0':
            k += 1

    else:
        k = 0
    max_count = max(m, k)
print(m)
