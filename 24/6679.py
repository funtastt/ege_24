s = open('../24.txt').readline()

for ch in s:
    if ch not in '0123456789ABCDEFGHIJKLMNOPQRST_':
        s = s.replace(ch, '_')

numbers = [t for t in s.split('_') if t]

max_len = 0
max_string = '0'

for number in numbers:
    if number[0] == '0':
        continue
    isCorrect = True
    for i in range(len(number) - 1):
        if (int(number[i], 30) - int(number[i + 1], 30)) % 2 == 0:
            isCorrect = False

    if isCorrect:
        if len(number) > max_len:
            max_string = number
            max_len = len(number)
        elif len(number) == max_len:
            if int(number, 30) < int(max_string, 30):
                max_string = number



print(max_string)