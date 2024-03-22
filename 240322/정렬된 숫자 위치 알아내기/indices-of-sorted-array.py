n = int(input())
nums = list(map(int, input().split()))

answer = []

for i in range(n):
    nums[i] = (nums[i], i+1)
sorted_nums = sorted(nums, key=lambda x: (x[0], x[1]))

for num in nums:
    idx = sorted_nums.index(num)
    answer.append(idx+1)

for elem in answer:
    print(elem, end=" ")