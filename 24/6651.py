s = open('../24.txt').readline().replace('BAD', '.').replace('FAT', '.')

lens = [len(k) for k in s.split('.')][1:-1]

print(min(a+b for a, b in zip(lens, lens[1:])) + 9)