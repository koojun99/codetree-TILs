def add(n):
    if n == 1:
        return 1
    return add(n-1) + n

n = int(input())
print(add(n))