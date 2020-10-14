import tkinter

def click_btn():
    pts = 0
    for i in range(7):
        if bvar[i].get() == True:
            pts = pts + 1
    text.delete("1.0", tkinter.END)
    text.insert("1.0", "체크된 수는 " + str(pts))

root = tkinter.Tk()
root.title("고양이 지수 진단 게임")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="mina.png")
canvas.create_image(400, 300, image=gazou)
button = tkinter.Button(text="진단하기", font=("Times New Roman", 32), bg="lightgreen", command=click_btn)
button.place(x=400, y=480)
text = tkinter.Text(width=40, height=5, font=("Times New Roman", 16))
text.place(x=320, y=30)

bvar = [None] * 7
cbtn = [None] * 7
ITEM = [
    "높은 곳이 좋다",
    "공을 보면 굴리고 싶어진다",
    "깜짝 놀라면 털이 곤두선다",
    "쥐구멍이 마음에 든다",
    "개에게 적대감을 느낀다",
    "생선 뼈를 발라 먹고 싶다",
    "밤, 기운이 난다"
]
for i in range(7):
    bvar[i] = tkinter.BooleanVar()
    bvar[i].set(False)
    cbtn[i] = tkinter.Checkbutton(text=ITEM[i], font=("Times New Roman", 12), variable=bvar[i], bg="#dfe")
    cbtn[i].place(x=400, y=160 + 40 * i)
root.mainloop()
