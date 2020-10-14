import random
import datetime
ALP = ["A", "B", "C", "D", "E", "F", "G"]
r = random.choice(ALP)
alp = ""
for i in ALP:
    if i != r:
        alp = alp + i
print(alp)
st = datetime.datetime.now()
ans = input("빠진 알파벳은?")
if ans == r:
    print("정답입니다")
    et = datetime.datetime.now()
    print((et - st).seconds)
else:
    print("틀렸습니다")
