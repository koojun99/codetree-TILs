string = input()
answer = []
for i in range(len(string)):
    if i%2 != 0:
        answer.append(string[i])

reverse = answer[::-1]
print("".join(reverse))