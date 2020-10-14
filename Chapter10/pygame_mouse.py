import pygame
import sys

BLACK = (0, 0, 0)
LBLUE = (0, 192, 255)
PINK = (255, 0, 224)

def main():
    pygame.init()
    pygame.display.set_caption("첫 번째 Pygame: 마우스 입력")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 60)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mouseX, mouseY = pygame.mouse.get_pos()
        txt1 = font.render("{},{}".format(mouseX, mouseY), True, LBLUE)

        mBtn1, mBtn2, mBtn3 = pygame.mouse.get_pressed()
        txt2 = font.render("{}:{}:{}".format(mBtn1, mBtn2, mBtn3), True, PINK)

        screen.fill(BLACK)
        screen.blit(txt1, [100, 100])
        screen.blit(txt2, [100, 200])
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
