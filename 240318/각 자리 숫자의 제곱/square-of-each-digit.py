def sum_power(n):
    if n < 10:
        return n**2
    return sum_power(n//10) + (n%10)**2

n = int(input())
print(sum_power(n))