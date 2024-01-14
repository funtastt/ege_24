words = (open('../24.txt').readline()
     .replace('A', '_')
     .replace('E', '_')
     .replace('Y', '_')
     .replace('U', '_')
     .replace('I', '_')
     .replace('O', '_')).split('_')

print(max(len(s) for s in words if s.count('.') >= 6))