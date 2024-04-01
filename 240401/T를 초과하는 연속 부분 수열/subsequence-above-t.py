n, t = map(int, input().split())
nums = list(map(int, input().split()))
max_size = 0
size = 0

for i in range(len(nums)):
    if nums[i] > t:
        if i > 0 and nums[i] > nums[i-1]:
            size += 1
        else:
            size = 1
    else:
        size = 0
    max_size = max(max_size, size)

print(max_size)