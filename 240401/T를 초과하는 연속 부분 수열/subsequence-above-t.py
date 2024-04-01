n, t = map(int, input().split())
nums = list(map(int, input().split()))
max_size = 0
size = 0

# 연속 부분 수열을 찾기 위해 nums 리스트를 순회
for num in nums:
    if num > t:
        size += 1
        max_size = max(max_size, size)
    else:
        size = 0  # t보다 큰 수가 아니라면, size를 0으로 리셋

print(max_size)