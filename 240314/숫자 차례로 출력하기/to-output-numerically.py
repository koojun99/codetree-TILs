def nums(n):
    if n == 0:
        return
    nums(n-1)
    print(n, end = " ")

def reversed_nums(n):
    if n == 0:
        return
    print(n, end = " ")
    reversed_nums(n-1)
    

n = int(input())

nums(n)
print()
reversed_nums(n)