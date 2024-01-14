line = open('../24.txt').readline()

k = 0
for i in range(len(line) - 2):
    unique = {line[i], line[i + 1]}

    for j in range(i + 2, len(line)):
        unique.add(line[j])
        if len(unique) == 3:
            break
        else:
            k += 1

print(k)
