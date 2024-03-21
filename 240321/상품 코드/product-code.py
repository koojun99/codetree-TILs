class Item:
    def __init__(self, name, code):
        self.name = name
        self.code = code

name, code = input().split()
codetree = Item("codetree", "50")
leebros = Item(name, code)

print("product " + codetree.code + " is " + codetree.name)
print("product " + leebros.code + " is " + leebros.name)