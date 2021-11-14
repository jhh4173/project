import pygame  # 1. pygame 선언
import random
import os

pygame.init()  # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언

BLACK = (0, 0, 0)
size = [600, 800]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

def runGame():
    j_image = pygame.image.load('c:/open/jj.png')
    j_image = pygame.transform.scale(j_image, (50, 50))
    js = []

    for i in range(5):
        rect = pygame.Rect(j_image.get_rect())
        rect.left = random.randint(0, size[0])
        rect.top = -100
        dy = random.randint(3, 9)
        js.append({'rect': rect, 'dy': dy})

    u_image = pygame.image.load('c:/open/uu.png')
    u_image = pygame.transform.scale(u_image, (100, 100))
    u = pygame.Rect(u_image.get_rect())
    u.left = size[0] // 2 - u.width // 2
    u.top = size[1] - u.height
    u_dx = 0
    u_dy = 0

    global done
    while not done:
        clock.tick(30)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    u_dx = -5
                elif event.key == pygame.K_RIGHT:
                    u_dx = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    u_dx = 0
                elif event.key == pygame.K_RIGHT:
                    u_dx = 0

        for j in js:
            j['rect'].top += j['dy']
            if j['rect'].top > size[1]:
                js.remove(j)
                rect = pygame.Rect(j_image.get_rect())
                rect.left = random.randint(0, size[0])
                rect.top = -100
                dy = random.randint(3, 9)
                js.append({'rect': rect, 'dy': dy})

        u.left = u.left + u_dx

        if u.left < 0:
            u.left = 0
        elif u.left > size[0] - u.width:
            u.left = size[0] - u.width

        screen.blit(u_image, u)

        for j in js:
            if j['rect'].colliderect(u):
                done = True
            screen.blit(j_image, j['rect'])

        pygame.display.update()


runGame()
pygame.quit()

