string = input()

for char in string:
    if ord('A') <= ord(char) <= ord('Z'):
        print(char.lower(), end="")
    else:
        print(char.upper(), end="")