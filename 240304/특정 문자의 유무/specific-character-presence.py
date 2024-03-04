line = input()
isEe = False
isAb = False

if ('ee' in line):
    isEe = True
if ('ab' in line):
    isAb = True

if isEe:
    print("Yes", end= " ")
else:
    print("No", end= " ")

if isAb:
    print("Yes")
else:
    print("No")