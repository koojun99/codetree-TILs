given = input()
target = input()
def check():
    if target in given:
        return given.find(target)
    else:
        return -1

print(check())