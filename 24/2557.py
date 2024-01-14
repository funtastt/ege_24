lines = open('24.txt').readlines()

k = 0

for s in lines:
    for i in range(len(s) - 2):
        if s[i] == 'F' and s[i + 2] == 'O':
            k += 1
            break
print(k)
