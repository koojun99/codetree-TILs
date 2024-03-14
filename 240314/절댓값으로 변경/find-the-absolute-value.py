def to_abs(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])

n = int(input())
nums = list(map(int, input().split()))
to_abs(nums)
for elem in nums:
    print(elem, end=" ")