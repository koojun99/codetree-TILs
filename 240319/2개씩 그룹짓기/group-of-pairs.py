n = int(input())
nums = list(map(int, input().split()))
nums.sort()
candidates = []

for i in range(n):
    cadidate = nums[i] + nums[-1-i]
    candidates.append(cadidate)
print(max(candidates))