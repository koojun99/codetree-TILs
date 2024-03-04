line = input()
n = len(line)
answer = line[:1] + 'a' + line[2:-2] + 'a' + line[-1]
print(answer)