class GameCharacter:
    def __init__(self, job, life):
        self.job = job
        self.life = life

    def info(self):
        print(self.job)
        print(self.life)

human1 = GameCharacter("전사", 120)
human1.info()

human2 = GameCharacter("마법사", 80)
human2.info()
