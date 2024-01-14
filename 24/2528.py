s = open('../24.txt').readline()

curr = ''
max_num = 0

for ch in s:
    if ch in '0123456789':
        curr += ch
    elif curr:
        all_even = True
        for digit in curr:
            if int(digit) % 2 != 0:
                all_even = False
                break
        if all_even:
            max_num = max(max_num, int(curr))
        curr = ''

print(max_num)
