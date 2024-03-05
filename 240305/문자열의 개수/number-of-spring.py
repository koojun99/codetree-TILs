count = 0
answer = []
while True:
    string = input()
    if string == "0":
        break
    answer.append(string)
print(len(answer))
for i in range(len(answer)):
    if i % 2 == 0:
        print(answer[i])