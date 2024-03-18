def add(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return add(n-2) + n

n = int(input())
print(add(n))