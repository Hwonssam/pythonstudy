from email.utils import parseaddr
from msilib.schema import EventMapping
import pygame
################################################################################
#기본초기화 (반드시 해야하는 것들)
pygame.init()

#화면크기
screen_width = 480
screen_heingt = 640
screen = pygame.display.set_mode((screen_width, screen_heingt))

#화면 타이틀
pygame.display.set_caption("훤님 게임") #게임이름

# FPS
clock = pygame.time.Clock()
################################################################################
# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

#이벤트 루프
running = True
while running:
    dt = clock.tick(30) #게임화면의 초당프레임

    #2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
    #3. 게임 캐릭터 위치 정의

    #4. 충돌 처리

    #5. 화면에 그리기
    pygame.display.update() #게임화면 계속 그리기

#pygame 종료
pygame.quit()