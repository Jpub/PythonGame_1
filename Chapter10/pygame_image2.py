import pygame

WHITE = (255, 255, 255)
NAVY = (0, 0, 128)


def main():
    pygame.init()
    pygame.display.set_caption("첫번째 Pygame: 화면 회전, 확대/축소")
    screen = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)
    img = pygame.image.load("pg_slime.png")
    tmr = 0

    while True:
        tmr = tmr + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        ang = (tmr % 36) * 10
        per = (tmr % 100) / 20
        img_s = pygame.transform.scale(img, [70, 92])
        img_r = pygame.transform.rotate(img, ang)
        img_rz = pygame.transform.rotozoom(img, ang, per)

        screen.fill(NAVY)
        screen.blit(img, [100, 100])
        screen.blit(img_s, [200, 100])
        screen.blit(img_r, [300, 100])
        screen.blit(img_rz, [400, 100])

        txt = font.render(str(tmr), True, WHITE)
        screen.blit(txt, [50, 50])

        pygame.display.update()
        clock.tick(10)


if __name__ == '__main__':
    main()
