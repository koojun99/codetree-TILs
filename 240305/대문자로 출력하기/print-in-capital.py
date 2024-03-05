line = input()

for char in line:
    if char.isalpha():
        print(char.upper(), end="")