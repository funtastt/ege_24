string = open('../24.txt').readline()
curr = ""
max_len = 0

for char in string:
    if (not char.isdigit() or not curr[-1].isdigit()) or (int(char) % 2 == int(curr[-1]) % 2):
        curr += char
    else:
        curr = char

    max_len = max(max_len, len(curr))

print(max_len)
