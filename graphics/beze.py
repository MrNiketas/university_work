import pygame

BLACK = (0, 0, 0)
WHITE = (100, 100, 100)
RED = (34,139,34)
dots = []
curve = []
press = 0

pygame.init()
screen = pygame.display.set_mode((1920, 800))
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                dots = []
                curve = []
                press = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if press == 0:
                    press = 1
                    dots = [event.pos, event.pos, event.pos, event.pos]
                elif press == 1:
                    press = 2
                elif press == 2:
                    press = 3
                elif press == 3:
                    press = -1

        if event.type == pygame.MOUSEMOTION:
            if press == 1:
                dots[3] = event.pos
            elif press == 2:
                dots[2] = event.pos
            elif press == 3:
                dots[1] = event.pos
    screen.fill(BLACK)
    if dots:
        pygame.draw.aalines(screen, WHITE, False, dots)
        for dot in dots:
            pygame.draw.circle(screen, WHITE, dot, 5, 1)
        curve = []
        for i in map(lambda x: x/100.0, range(0, 105, 5)):
            x = (1.0-i)**3*dots[0][0] + 3*(1.0-i)**2*i*dots[1][0] + 3*(1.0-i)*i**2*dots[2][0] + i**3*dots[3][0]
            y = (1.0-i)**3*dots[0][1] + 3*(1.0-i)**2*i*dots[1][1] + 3*(1.0-i)*i**2*dots[2][1] + i**3*dots[3][1]
            curve.append([x, y])
        pygame.draw.lines(screen, RED, False, curve, 3)

    pygame.display.flip()
    clock.tick(30)