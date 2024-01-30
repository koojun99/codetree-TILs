def is_beautiful(arr):
    i = 0
    while i < len(arr):
        num = arr[i]
        count = 0
        while i < len(arr) and arr[i] == num:
            count += 1
            i += 1
        if count != num:
            return False
    return True

def count_beautiful_numbers(n, arr=[], count=0):
    if len(arr) == n:
        if is_beautiful(arr):
            return 1
        else:
            return 0
    total = 0
    for i in range(1, 5):
        arr.append(i)
        total += count_beautiful_numbers(n, arr, count)
        arr.pop()
    return total

n = int(input())
print(count_beautiful_numbers(n))