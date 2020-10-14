import tkinter

FNT1 = ("Times New Roman", 12)
FNT2 = ("Times New Roman", 24)

WORDS = [
    "apple", "사과",
    "book", "책",
    "cat", "고양이",
    "dog", "개",
    "egg", "계란",
    "fire", "불",
    "gold", "금색",
    "head", "머리",
    "ice", "얼음",
    "juice", "주스",
    "king", "왕",
    "lemon", "레몬",
    "mother", "엄마",
    "notebook", "공책",
    "orange", "오렌지",
    "pen", "펜",
    "queen", "여왕",
    "room", "방",
    "sport", "운동",
    "time", "시간",
    "user", "사용자",
    "vet", "수의사",
    "window", "창",
    "xanadu", "무릉도원",
    "yellow", "노랑",
    "zoo", "동물원"
]
MAX = int(len(WORDS) / 2)
score = 0
word_num = 0
yourword = ""
koff = False  # 1 문자씩 입력하기 위한 플래그

def key_down(e):
    global score, word_num, yourword, koff
    if koff == True:
        koff = False
        kcode = e.keycode
        ksym = e.keysym
        if 65 <= kcode and kcode <= 90:  # 영문자 대문자
            yourword = yourword + chr(kcode + 32)
        if 97 <= kcode and kcode <= 122:  # 영문자 소문자
            yourword = yourword[:-1]  # 맨 끝 1 문자 삭제
        if ksym == "Delete" or ksym == "BackSpace":
            yourword = yourword[:-1]  # 맨 끝 한 문자 삭제
        input_label["text"] = yourword
        if ksym == "Return":
            if input_label["text"] == english_label["text"]:
                score = score + 1
                set_label()

def key_up(e):
    global koff
    koff = True

def set_label():
    global word_num, yourword
    score_label["text"] = score
    english_label["text"] = WORDS[word_num * 2]
    korean_label["text"] = WORDS[word_num * 2 + 1]
    input_label["text"] = ""
    word_num = (word_num + 1) % MAX
    yourword = ""

root = tkinter.Tk()
root.title("영어 학습 애플리케이션")
root.geometry("400x200")
root.resizable(False, False)
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
root["bg"] = "#DEF"

score_label = tkinter.Label(font=FNT1, bg="#DEF", fg="#4C0")
score_label.pack()
english_label = tkinter.Label(font=FNT2, bg="#DEF")
english_label.pack()
korean_label = tkinter.Label(font=FNT1, bg="#DEF", fg="#444")
korean_label.pack()
input_label = tkinter.Label(font=FNT2, bg="#DEF")
input_label.pack()
howto_label = tkinter.Label(text="영어 단어를 입력하고 [Enter] 키를 누릅니다.\n입력을 수정할 때는 [Delete] 혹은 [BackSpace]", font=FNT1, bg="#FFF", fg="#ABC")
howto_label.pack()

set_label()
root.mainloop()
