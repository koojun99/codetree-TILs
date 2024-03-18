def cal(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return cal(n//3) + cal(n-1)

n = int(input())
print(cal(n))