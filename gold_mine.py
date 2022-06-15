# 기본 뼈대 생성
import os
import pygame

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gold Miner")

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
background = pygame.image.load(os.path.join(current_path, "background.png"))

running = True
# 게임실행
while running:
    clock.tick(30)  # fps 값이 30으로 고정

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    pygame.display.update()

pygame.quit()
