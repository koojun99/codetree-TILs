line = input()
print(line)
answer = line
for _ in range(len(line)):
    answer = answer[-1] + answer[:-1]
    print(answer)