def cal(n):
    if n == 1:
        return 2
    if n == 2:
        return 4
    return cal(n-2) * cal(n-1) % 100

n = int(input())
print(cal(n))