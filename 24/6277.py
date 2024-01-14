s = open('../24.txt').readline()

max_len = 0
max_ch = ''

for ch in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    curr_max = max(len(t) for t in s.split(ch)[1:-1])

    if max_len <= curr_max:
        max_len = curr_max
        max_ch = ch

print(max_ch + str(max_len + 2))