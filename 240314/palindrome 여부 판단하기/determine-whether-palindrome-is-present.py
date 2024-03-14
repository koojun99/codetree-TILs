def is_palindrome(string):
    reverse = string[::-1]
    if string == reverse:
        print("Yes")
    else:
        print("No")

string = input()
is_palindrome(string)