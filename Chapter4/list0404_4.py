import random

cnt = 0
while True:
    r = random.randint(1, 100)
    print(r)
    cnt = cnt + 1
    if r == 77:
        break
print(str(cnt) + "번째에 희귀 캐릭터 겟!")
