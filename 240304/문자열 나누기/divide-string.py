n = int(input())
nums = list(input().split())
answer = ""

for num in nums:
    for i in range(len(num)):
        answer += num[i]
        if len(answer) == 5:
            print(answer)
            answer = ""
print(answer)