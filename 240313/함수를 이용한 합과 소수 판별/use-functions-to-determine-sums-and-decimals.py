def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def isEven(n):
    result = 0
    while n > 0:
        result += n % 10
        n = n // 10
    if result % 2 == 0:
        return True
    return False

a, b = map(int, input().split())
count = 0

for i in range(a, b+1):
    if is_prime(i):
        if isEven(i):
            count += 1
print(count)