class User:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
name, level = input().split()
codetree = User("codetree", "10")
hello = User(name, level)

print("user " + codetree.name + " lv " + codetree.level)
print("user " + hello.name + " lv " + hello.level)