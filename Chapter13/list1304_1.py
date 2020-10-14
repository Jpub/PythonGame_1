class Human:
    def __init__(self, name, life):
        self.name = name
        self.life = life

    def info(self):
        print(self.name)
        print(self.life)


class Soldier(Human):
    def __init__(self, name, life, weapon):
        super().__init__(name, life)
        self.weapon = weapon

    def info(self):
        print("내 이름은 " + self.name)
        print("내 체력은 {}".format(self.life))

    def talk(self):
        print(self.weapon + "을(를) 장비하고, 모험을 시작합니다.")


man = Human("톰(일반인)", 50)
man.info()
print("----------")
prince = Soldier("알렉스(왕자)", 200, "빛의 검")
prince.info()
prince.talk()
