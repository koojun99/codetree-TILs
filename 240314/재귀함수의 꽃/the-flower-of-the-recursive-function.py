def calculate(n):
    if n == 0:
        return
    print(n, end=" ")
    calculate(n-1)
    print(n, end=" ")

n = int(input())
calculate(n)