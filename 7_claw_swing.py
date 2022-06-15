# 집게까지 직선을 그리기
import os
import pygame

# 집게 클래스


class Claw(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.original_image = image
        self.rect = image.get_rect(center=position)

        # 집게를 약간 오른쪽으로 이동시키기 위함
        self.offset = pygame.math.Vector2(defalut_offset_x_claw, 0)
        self.position = position

        self.direction = LEFT  # 집게의 이동 방향
        self.angle_speed = 2.5  # 집게의 각도 변경 폭 (좌우 이동 속도)
        self.angle = 10  # 최초 각도 정의(오른쪽 끝)

    # rect를 업데이트 하기 위함
    # 처음 이미지 보다 살짝 오른쪽으로 땡길 수 있음

    def update(self):
        if self.direction == LEFT:  # 왼쪽 방향으로 이동하고 있다면
            self.angle += self.angle_speed  # 이동 속도 만큼 각도 증가
        elif self.direction == RIGHT:  # 오른쪽 방향으로 이동하고 있다면
            self.angle -= self.angle_speed

      # 만약에 허용 각도 범위를 벗어나면?
        if self.angle > 170:
            self.angle = 170
            self.direction = RIGHT
        elif self.angle < 10:
            self.angle = 10
            self.direction = LEFT

        self.rotate()  # 회전 처리

        # rect_center = self.position + self.offset
        # self.rect = self.image.get_rect(center=rect_center)
    def rotate(self):
        # 이미지 회전
        self.image = pygame.transform.rotozoom(
            self.original_image, -self.angle, 1)
        # 회전 대상 이미지 , 회전시킬 각도, 이미지 크기

        offset_rotated = self.offset.rotate(self.angle)

        self.rect = self.image.get_rect(center=self.position + offset_rotated)
        # 범위를 벗어나지 않고 그림을 그려줌

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # rect에 해당하는 위치
        pygame.draw.circle(screen, RED, self.position, 3)  # 중심점 표시
        # 직선그리기
        pygame.draw.line(screen, BLACK, self.position, self.rect.center, 5)
        #                스크린에 그림 , 검정, 집게의 위치,  , 직선의 두께

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

# 게임 관련 변수
defalut_offset_x_claw = 40  # 중심점으로부터 집게까지의 기본 x 간격
LEFT = -1  # 왼쪽 방향
RIGHT = 1  # 오른쪽 방향

# 색깔 변수
RED = (255, 0, 0)
BLACK = (0, 0, 0)  # 직선을 사용

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

# 집게
claw_image = pygame.image.load(os.path.join(current_path, "claw.png"))
# 가로위치는 화면 가로 기준으로 절반, 세로 위치는 위에서 110px
claw = Claw(claw_image, (screen_width // 2, 110))

running = True
# 게임실행
while running:
    clock.tick(30)  # fps 값이 30으로 고정

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    gemstone_group.draw(screen)  # 그룹 내 모든 스프라이트를 screen에 그림
    # 집게 이미지 업데이트 후 그림을 그림
    claw.update()
    claw.draw(screen)
    pygame.display.update()

pygame.quit()
