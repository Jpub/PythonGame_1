import pygame
import sys

WHITE = (255, 255, 255)

imgBtlBG = pygame.image.load("btlbg.png")
imgEnemy = None

emy_num = 0
emy_x = 0
emy_y = 0

def init_battle():
    global imgEnemy, emy_num, emy_x, emy_y
    emy_num = emy_num + 1
    if emy_num == 5:
        emy_num = 1
    imgEnemy = pygame.image.load("enemy" + str(emy_num) + ".png")
    emy_x = 440 - imgEnemy.get_width() / 2
    emy_y = 560 - imgEnemy.get_height()

def draw_battle(bg, fnt):
    bg.blit(imgBtlBG, [0, 0])
    bg.blit(imgEnemy, [emy_x, emy_y])
    sur = fnt.render("enemy" + str(emy_num) + ".png", True, WHITE)
    bg.blit(sur, [360, 580])

def main():
    pygame.init()
    pygame.display.set_caption("전투 개시 처리")
    screen = pygame.display.set_mode((880, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)

    init_battle()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    init_battle()

        draw_battle(screen, font)
        pygame.display.update()
        clock.tick(5)

if __name__ == '__main__':
    main()
