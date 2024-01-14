string = open('../24.txt').readline()

max_count = 0
curr = 1

for i in range(len(string) - 1):
    if string[i] != string[i+1]:
        curr += 1
    else:
        curr = 1
    max_count = max(max_count, curr)
print(max_count)
