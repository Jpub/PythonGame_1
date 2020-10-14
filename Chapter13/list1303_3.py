import tkinter
import time
FNT = ("Times New Roman", 24)

class GameCharacter:
    def __init__(self, name, life, x, y, imgfile, tagname):
        self.name = name
        self.life = life
        self.lmax = life
        self.x = x
        self.y = y
        self.img = tkinter.PhotoImage(file=imgfile)
        self.tagname = tagname

    def draw(self):
        x = self.x
        y = self.y
        canvas.create_image(x, y, image=self.img, tag=self.tagname)
        canvas.create_text(x, y + 120, text=self.name, font=FNT, fill="red", tag=self.tagname)
        canvas.create_text(x, y + 200, text="life{}/{}".format(self.life, self.lmax), font=FNT, fill="lime",
                           tag=self.tagname)

    def attack(self):
        di = 1
        if self.x >= 400:
            di = -1
        for i in range(5):  # 공격 동작(옆으로 움직임)
            canvas.coords(self.tagname, self.x + i * 10 * di, self.y)
            canvas.update()
            time.sleep(0.1)
        canvas.coords(self.tagname, self.x, self.y)

    def damage(self):
        for i in range(5):  # 데미지(화면 깜빡임)
            self.draw()
            canvas.update()
            time.sleep(0.1)
            canvas.delete(self.tagname)
            canvas.update()
            time.sleep(0.1)
        self.life = self.life - 30
        if self.life > 0:
            self.draw()
        else:
            print(self.name + "은 쓰러졌다... ")

def click_left():
    character[0].attack()
    character[1].damage()

def click_right():
    character[1].attack()
    character[0].damage()

root = tkinter.Tk()
root.title("객체 지향을 활용한 전투")
canvas = tkinter.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

btn_left = tkinter.Button(text="공격 →", command=click_left)
btn_left.place(x=160, y=560)
btn_right = tkinter.Button(text="← 공격", command=click_right)
btn_right.place(x=560, y=560)

character = [
    GameCharacter("태양의 검사 「가이아」", 200, 200, 280, "swordsman.png", "LC"),
    GameCharacter("어둠의 닌자 「한조」", 160, 600, 280, "ninja.png", "RC")
]
character[0].draw()
character[1].draw()

root.mainloop()
