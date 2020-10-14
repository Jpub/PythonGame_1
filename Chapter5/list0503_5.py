import random
pl_pos = 1
com_pos = 1
def board():
    print("•" * (pl_pos - 1) + "Ｐ" + "•" * (30 - pl_pos) + "Goal")
    print("•" * (com_pos - 1) + "Ｃ" + "•" * (30 - com_pos) + "Goal")

board()
print("주사위 게임, 스타트!")
while True:
    input("Enter를 누르면 여러분의 말이 움직입니다")
    pl_pos = pl_pos + random.randint(1, 6)
    if pl_pos > 30:
        pl_pos = 30
    board()
    if pl_pos == 30:
        print("당신이 승리했습니다！")
        break
    input("Enter를 누르면 컴퓨터의 말이 움직입니다")
    com_pos = com_pos + random.randint(1, 6)
    if com_pos > 30:
        com_pos = 30
    board()
    if com_pos == 30:
        print("컴퓨터가 승리했습니다!")
        break
