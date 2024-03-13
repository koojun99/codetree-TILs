def season(month):
    if 1 <= month <=2 or month == 12:
        print("Winter")
    if 3 <= month <= 5:
        print("Spring")
    if 6 <= month <= 8:
        print("Summer")
    if 9 <= month <= 11:
        print("Fall")

def isYoon(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def isValid(year, month, day):
    thirty = [4, 6, 9, 11]
    if month == 2:
        if isYoon(year):
            if day > 29:
                return False
            else:
                return True
        if day > 28:
            return False
    if month in thirty:
        if day > 30:
            return False
    else:
        if day > 31:
            return False
    return True

y, m, d = map(int, input().split())

if isValid(y, m, d):
    season(m)
else:
    print(-1)