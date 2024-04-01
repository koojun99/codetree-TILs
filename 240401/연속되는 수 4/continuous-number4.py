size = 0
max_size = 0
nums = []
n = int(input())

for _ in range(n):
    nums.append(int(input()))

for i in range(len(nums)):
    if i > 0 and nums[i] > nums[i-1]:
        size += 1
    max_size = max(max_size, size)

print(max_size)