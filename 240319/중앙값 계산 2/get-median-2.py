def median(arr):
    arr.sort()
    pos = len(arr) // 2
    return arr[pos]

n = int(input())
nums = list(map(int, input().split()))

for i in range(n):
    if i % 2 == 0:
        print(median(nums[:i+1]), end=" ")