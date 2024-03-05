char = input()
ascii = ord(char)
print(chr((ascii+1)%127))