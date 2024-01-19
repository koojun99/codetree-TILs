string = input()
answer = []
count = 1
answer. append(string[0])

for i in range(1, len(string)):
    if string[i] == string[i-1]:
        count += 1
    else:
        answer.append(str(count))
        answer.append(string[i])
        count = 1
answer.append(str(count))
result = "".join(answer)

print(len(result))
print(result)