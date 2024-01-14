lines = open('24.txt').readlines()

k = 0

for s in lines:
    for i in range(len(s) - 2):
        if s[i] == 'A' and s[i + 2] == 'R':
            k += 1
            break
print(k)
