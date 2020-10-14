import tkinter
root = tkinter.Tk()
root.title("처음부터 체크된 상태 만들기")
root.geometry("400x200")
cval = tkinter.BooleanVar()
cval.set(True)
cbtn = tkinter.Checkbutton(text="체크 버튼", variable=cval)
cbtn.pack()
root.mainloop()
