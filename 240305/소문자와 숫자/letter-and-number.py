line = input()

for char in line:
    if char.isalpha() or char.isdigit():
        print(char.lower(), end="")