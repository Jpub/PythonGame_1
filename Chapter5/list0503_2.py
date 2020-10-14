pl_pos = 6
com_pos = 3
def board():
    print("•" * (pl_pos - 1) + "Ｐ" + "•" * (30 - pl_pos))
    print("•" * (com_pos - 1) + "Ｃ" + "•" * (30 - com_pos))
board()
