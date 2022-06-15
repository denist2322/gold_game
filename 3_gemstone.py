# 기본 뼈대 생성
import os
import pygame

# 보석 클래스


class Gemstone(pygame.sprite.Sprite):
    def __init__(self, image, position):  # position은 보석의 위치
        super().__init__()
        # 캐릭터의 이미지
        self.image = image
        # 캐릭터의 정보
        self.rect = image.get_rect(center=position)


def setup_gemstone():
    # 작은 금
    # 0번째 이미지를 화면(200,380) 에 위치 (x,y)
    small_gold = Gemstone(gemstone_images[0], (200, 380))
    gemstone_group.add(small_gold)  # 그룹에 추가
    # 큰 금
    gemstone_group.add(Gemstone(gemstone_images[1], (300, 500)))
    # 돌
    gemstone_group.add(Gemstone(gemstone_images[2], (300, 380)))
    # 다이아몬드
    gemstone_group.add(Gemstone(gemstone_images[3], (900, 420)))


pygame.init()
# 보석 이미지 불러오기
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gold Miner")
clock = pygame.time.Clock()

# 배경 이미지 불러오기
current_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
background = pygame.image.load(os.path.join(current_path, "background.png"))

# 4개 보석 이미지 불러오기 (작은 금, 큰 금, 돌, 다이아몬드)
gemstone_images = [
    pygame.image.load(os.path.join(current_path, "small_gold.png")),  # 작은금
    pygame.image.load(os.path.join(current_path, "big_gold.png")),  # 큰 금
    pygame.image.load(os.path.join(current_path, "stone.png")),  # 돌
    pygame.image.load(os.path.join(current_path, "diamond.png"))]  # 다이아몬드

# pygame에서 제공하는 그룹
# 보석 그룹
gemstone_group = pygame.sprite.Group()
setup_gemstone()  # 게임에 원하는 만큼의 보석 정의

running = True
# 게임실행
while running:
    clock.tick(30)  # fps 값이 30으로 고정

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    gemstone_group.draw(screen)  # 그룹 내 모든 스프라이트를 screen에 그림
    pygame.display.update()

pygame.quit()
