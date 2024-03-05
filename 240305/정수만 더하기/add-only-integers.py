line = input()
answer = 0
for char in line:
    if char.isdigit():
        answer += int(char)
print(answer)