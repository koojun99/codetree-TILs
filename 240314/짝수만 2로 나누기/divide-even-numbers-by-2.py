def divideByTwo(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = arr[i]//2

n = int(input())
nums = list(map(int, input().split()))
divideByTwo(nums)

for i in range(n):
    print(nums[i], end= " ")