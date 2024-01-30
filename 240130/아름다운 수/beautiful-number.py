n = int(input())

def count_beautiful_numbers(n, start=1):
    if n == 0:
        return 1
    count = 0
    for i in range(start, 5):
        if n >= i:
            count += count_beautiful_numbers(n - i, i)
    return count

print(count_beautiful_numbers(n))