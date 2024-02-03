def lds_length(nums):
    N = len(nums)
    dp = [1] * N  # 모든 위치에서 LDS의 초기 길이는 1입니다.
    
    for i in range(N):
        for j in range(i):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# 입력 예제
N = int(input())
nums = list(map(int, input().split()))

# 출력
print(lds_length(nums))