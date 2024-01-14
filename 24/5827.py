line = open('24.txt').readline()
for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    line = line.replace(ch, '.')

nums = [int(n) for n in line.split('.') if len(n) > 0 and not n.startswith('0')]
print(max(nums))