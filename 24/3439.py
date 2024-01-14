s = open('../24.txt').readline()

print(sum(1 for i in range(len(s) // 2) if s[i] == s[len(s) - i - 1]))