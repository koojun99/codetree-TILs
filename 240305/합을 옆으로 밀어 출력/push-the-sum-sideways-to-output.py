n = int(input())
answer = 0

for _ in range(n):
    answer += int(input())
string = str(answer)

print(string[1:] + string[0])