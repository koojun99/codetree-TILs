def max_num(i, num, nums):
    if i == len(nums)-1:
        return num
    if nums[i] > num:
        num = nums[i]
    return max_num(i+1, num, nums)

n = int(input())
num = 0
nums = list(map(int, input().split()))
print(max_num(0, num, nums))