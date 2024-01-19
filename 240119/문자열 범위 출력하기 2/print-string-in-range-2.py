string = input()
n = int(input())
string = string.replace(" ","")
extracted = string[-n:]

print(extracted[::-1])