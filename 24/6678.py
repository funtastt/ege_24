s = open('24.txt').readline()

for ch in s:
    if ch not in '0123456789ABCDEFGHI_':
        s = s.replace(ch, '_')

numbers = [t for t in s.split('_') if t]

max_string = '0'

for number in numbers:
    if number[0] == '0':
        continue

    if int(number[-1], 19) % 2 == 0:
        if int(number, 19) > int(max_string, 19):
            max_string = number

print(max_string)
