n = int(input())
nums = [int(input()) for _ in range(n)]

answer, count = 0, 0

for i in range(n):
    if i > 0 and nums[i] * nums [i-1] < 0:
        count = 1
    else:
        count += 1
    answer = max(answer, count)

print(answer)