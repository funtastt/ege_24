count = 0

with open('../24.txt') as file:
    for s in file:
        chars = ['Q', 'W', 'E', 'R', 'T', 'Y']

        all_good = True
        for ch in chars:
            if ch in s:
                s = s[s.find(ch):]
            else:
                all_good = False
                break

        if all_good:
            count += 1
print(count)