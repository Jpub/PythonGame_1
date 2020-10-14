import tkinter
import tkinter.messagebox

def click_btn():
    tkinter.messagebox.showinfo("정보", "버튼을 눌렀습니다")

root = tkinter.Tk()
root.title("첫 번째 메시지 박스")
root.geometry("400x200")
btn = tkinter.Button(text="테스트", command=click_btn)
btn.pack()
root.mainloop()
