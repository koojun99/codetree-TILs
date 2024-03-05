string1 = input()
string2 = input()
list1 = []
list2 = []

for char in string1:
    if char.isdigit():
        list1.append(char)

for char in string2:
    if char.isdigit():
        list2.append(char)

num1 = int(''.join(list1))
num2 = int(''.join(list2))

print(num1 + num2)