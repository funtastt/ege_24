line = open('../24.txt').readline()

k = 0

for i in range(len(line)):
    if line[i] == '#':
        if all(ch <= 'F' and ch not in '#%&' for ch in line[i + 1:i + 7]):
            r, g, b = int(line[i + 1] + line[i + 2], 16), int(line[i + 3] + line[i + 4], 16), int(line[i + 5] + line[i + 6], 16)
            if r > g and r > b:
                k +=1

print(k)
