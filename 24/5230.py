string = open('../24.txt').readline()

curr = ''
max_len = 0
count = 0

for char in string:
    curr += char
    count += 1 if char in 'AEYUIO' else 0

    while count > 5:
        if curr[0] in 'AEYUIO':
            count -= 1
        curr = curr[1:]

    max_len = max(max_len, len(curr))

print(max_len)
