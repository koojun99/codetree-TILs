def is_different(string):
    last_char = string[0]
    for char in string:
        if last_char != char:
            return True
    return False
count = 1
string = input()
if is_different(string):
    print("Yes")
else:
    print("No")