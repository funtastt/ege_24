s = open('../24.txt').readline()

max_sum = 0
curr_sum = 0

for char in s:
    if char == '0':
        if curr_sum % 5 == 0:
            max_sum = max(max_sum, curr_sum)
        curr_sum = 0
    else:
        curr_sum += int(char)

print(max_sum)