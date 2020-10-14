QUESTION = [
    "유경자 씨의 남편의 이름은?",
    "이경수의 딸의 이름은?",
    "민주희 씨는 이경수 씨와 어떤 관계입니까?"]
R_ANS = ["정현철", "이현지", "조카"]
R_ANS2 = ["Hyunchul Jung", "Hyunji Lee", "niece"]

for i in range(3):
    print(QUESTION[i])
    ans = input()
    if ans == R_ANS[i] or ans == R_ANS2[i]:
        print("정답입니다")
    else:
        print("틀렸습니다")
