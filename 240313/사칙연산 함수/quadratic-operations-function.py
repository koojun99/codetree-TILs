a, o, c = input().split()


def operation(a, o, c):
    a = int(a)
    c = int(c)
    if o == "+":
        return a + c
    elif o == "-":
        return a - c
    elif o == "/":
        return a // c
    elif o == "*":
        return a * c
    else:
        return False
if not operation(a,o,c):
    operation(a, o, c)
else:
    print(a + " " + o + " " + c + " = " + str(operation(a,o,c)))