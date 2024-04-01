n, t = map(int, input().split())
nums = list(map(int, input().split()))
candidates = []
max_size = 0
size = 0

for i in range(len(nums)):
    if nums[i] > t:
        candidates.append(nums[i])

for i in range(len(candidates)):
    if i > 0 and candidates[i] > candidates[i-1]:
        size += 1
    else:
        size = 1
    max_size = max(max_size, size)

print(max_size)