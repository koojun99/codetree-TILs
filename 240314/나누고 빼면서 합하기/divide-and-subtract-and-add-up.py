def calculate(nums, m):
    answer = 0
    while m >= 1:
        answer += nums[m-1]
        if m % 2 == 0:
            m = m // 2
        else:
            m = m - 1
    print(answer)
n, m = map(int, input().split())
nums = list(map(int, input().split()))
calculate(nums, m)