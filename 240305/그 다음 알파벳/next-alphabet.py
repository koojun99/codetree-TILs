char = input()
ascii = ord(char)+1
if char == 'z':
    ascii = ord('a')
print(chr((ascii)))