def isYoon(year):
    if year % 100 == 0 and year % 400 != 0:
        return False
    if year % 4 == 0:
        return True
    return False

year = int(input())
if isYoon(year):
    print("true")
else:
    print("false")