import tkinter

key = ""
def key_down(e):
    global key
    key = e.keysym

def main_proc():
    label["text"] = key
    root.after(100, main_proc)

root = tkinter.Tk()
root.title("실시간 키입력")
root.bind("<KeyPress>", key_down)
label = tkinter.Label(font=("Times New Roman", 80))
label.pack()
main_proc()
root.mainloop()
