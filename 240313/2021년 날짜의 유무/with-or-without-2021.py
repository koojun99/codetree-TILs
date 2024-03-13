def is_Valid(month, day):
    thirty = [4, 6, 9, 11]
    if month > 12:
        return False
    if month == 2:
        if day > 28:
            return False
    if month in thirty:
        if day > 30:
            return False
    else:
        if day > 31:
            return False
    return True

m, d = map(int, input().split())

if is_Valid(m, d):
    print("Yes")
else:
    print("No")