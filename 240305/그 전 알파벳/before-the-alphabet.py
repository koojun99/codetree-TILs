char = input()
ascii = ord(char) - 1

if char == 'a':
    ascii = ord('z')

print(chr(ascii))