s = (open('../24.txt').readline()
     .replace('B', '_')
     .replace('E', '_')
     .replace('F', '_'))

print(max(len(string) for string in s.split('_')))