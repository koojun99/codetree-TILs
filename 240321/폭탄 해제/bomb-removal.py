class Bomb:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

code, color, sec = input().split()
bomb = Bomb(code, color, sec)
print("code : " + bomb.code)
print("color : " + bomb.color)
print("second : " + bomb.sec)