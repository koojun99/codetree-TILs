def gcd(a, b):
    if (b == 0):
         return a
    return gcd(b, a % b);

def lcm(a, b):
    return a*b // gcd(a, b)

n = int(input())
nums = list(map(int, input().split()))
num = nums[0]
for i in range(n):
    num = lcm(num, nums[i])

print(num)