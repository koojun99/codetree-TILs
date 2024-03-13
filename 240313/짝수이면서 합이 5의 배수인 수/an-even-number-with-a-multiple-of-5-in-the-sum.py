def isValid(n):
    a = n // 10
    b = n % 10
    if b % 2 == 0 and (a + b) % 5 == 0:
        print("Yes")
    else:
        print("No")
n = int(input())
isValid(n)