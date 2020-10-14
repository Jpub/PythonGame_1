import tkinter
root = tkinter.Tk()
root.title("첫 번째 버튼")
root.geometry("800x600")
button = tkinter.Button(root, text="버튼 문자열", font=("Times New Roman", 24))
button.place(x=200, y=100)
root.mainloop()
