def calculate(n, count):
    if n == 1:
        return count
    if n % 2 == 0:
        return calculate(n//2, count+1)
    else:
        return calculate(n*3 + 1, count+1)

n = int(input())
print(calculate(n, 0))