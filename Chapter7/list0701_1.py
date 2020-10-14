import tkinter
root = tkinter.Tk()
root.title("첫 번째 텍스트 입력 필드")
root.geometry("400x200")
entry = tkinter.Entry(width=20)
entry.place(x=10, y=10)
root.mainloop()
