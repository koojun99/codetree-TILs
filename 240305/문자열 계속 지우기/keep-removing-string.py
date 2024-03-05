line = input()
pattern = input()
n = len(pattern)
answer = line
while answer.find(pattern) != -1:
    pos = answer.find(pattern)
    answer = answer[:pos] + answer[pos+n:]
print(answer)