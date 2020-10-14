import tkinter
FNT = ("Times New Roman", 30)

class GameCharacter:
    def __init__(self, job, life, imgfile):
        self.job = job
        self.life = life
        self.img = tkinter.PhotoImage(file=imgfile)

    def draw(self, x, y):
        canvas.create_image(x + 200, y + 280, image=self.img)
        canvas.create_text(x + 300, y + 400, text=self.job, font=FNT, fill="red")
        canvas.create_text(x + 300, y + 480, text=self.life, font=FNT, fill="blue")

root = tkinter.Tk()
root.title("tkinter를 사용한 객체 지향 프로그래밍")
canvas = tkinter.Canvas(root, width=800, height=560, bg="white")
canvas.pack()

character = [
    GameCharacter("검사", 200, "swordsman.png"),
    GameCharacter("닌자", 160, "ninja.png")
]
character[0].draw(0, 0)
character[1].draw(400, 0)

root.mainloop()
