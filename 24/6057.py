lines = open('24.txt').readlines()

all_m = 0

for l in lines:
    m = 0
    k = 1
    ch = ''

    for i in range(1, len(l)):
        prev, curr = l[i-1], l[i]

        if prev == curr:
            k+=1
        else:
            k = 1
        if k >= m:
            m = k
            ch = curr

    if m >= all_m:
        all_m = m
        print(m, l.count(ch))
