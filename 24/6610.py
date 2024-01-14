words = open('../24.txt').readline().split('SOLO')

m = 0

for i in range(len(words) - 5):
    s = words[i] + words[i+1] + words[i+2] + words[i+3] + words[i+4]

    count = sum(1 for ch in '0123456789' if ch in s)

    if count >= 5:
        m = max(m, len(s))

print(m + 22)
