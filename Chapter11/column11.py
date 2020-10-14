import pygame
import sys
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    pygame.init()
    pygame.display.set_caption("반투명과 스크롤")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    surface_a = pygame.Surface((800, 600))
    surface_a.fill(BLACK)
    surface_a.set_alpha(32)

    CHIP_MAX = 50
    cx = [0] * CHIP_MAX
    cy = [0] * CHIP_MAX
    xp = [0] * CHIP_MAX
    yp = [0] * CHIP_MAX
    for i in range(CHIP_MAX):
        cx[i] = random.randint(0, 800)
        cy[i] = random.randint(0, 600)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.scroll(1, 4)
        screen.blit(surface_a, [0, 0])

        mx, my = pygame.mouse.get_pos()
        pygame.draw.rect(screen, WHITE, [mx - 4, my - 4, 8, 8])

        for i in range(CHIP_MAX):
            if mx < cx[i] and xp[i] > -20: xp[i] = xp[i] - 1
            if mx > cx[i] and xp[i] < 20: xp[i] = xp[i] + 1
            if my < cy[i] and yp[i] > -16: yp[i] = yp[i] - 1
            if my > cy[i] and yp[i] < 16: yp[i] = yp[i] + 1
            cx[i] = cx[i] + xp[i]
            cy[i] = cy[i] + yp[i]
            pygame.draw.circle(screen, (0, 64, 192), [cx[i], cy[i]], 12)
            pygame.draw.circle(screen, (0, 128, 224), [cx[i], cy[i]], 9)
            pygame.draw.circle(screen, (192, 224, 255), [cx[i], cy[i]], 6)

        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()
