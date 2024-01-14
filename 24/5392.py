text = open('../24.txt').readline()

digits = '0123456789'

max_len = curr = 0

for start_index in range(3):
    for i in range(start_index, len(text) - 2, 3):
        if text[i] not in digits and text[i + 1] in digits and text[i + 2] not in digits:
            curr += 1
            max_len = max(max_len, curr)
        else:
            curr = 0

print(max_len)
