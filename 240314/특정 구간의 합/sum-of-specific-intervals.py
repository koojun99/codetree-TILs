n, m = map(int, input().split())
nums = list(map(int, input().split()))

def calculate(a, b):
    global nums
    answer = 0
    for i in range(a-1, b):
        answer += nums[i]
    return answer

for _ in range(m):
    a, b = map(int, input().split())
    print(calculate(a, b))