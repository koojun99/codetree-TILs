n = int(input())
nums = []


for _ in range(n):
    num = int(input())
    nums.append(num)

counts = []
count = 1
for i in range(n):
    if i == 0 or nums[i] != nums[i-1]:
        counts.append(count)
        count = 1
    else:
        count += 1
counts.append(count)
    
print(max(counts))