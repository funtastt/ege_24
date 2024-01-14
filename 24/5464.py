text = open('../24.txt').readline()

curr = max_len = 0

for start_index in range(3):
    for i in range(start_index, len(text) - 2, 3):
        if text[i:i+3] == 'BAC' or text[i:i+3] == 'CAB':
            curr += 3
        else:
            max_len = max(max_len, curr)
            curr = 0

print(max_len)