from email.utils import parseaddr
from msilib.schema import EventMapping
import pygame
import random
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
background = pygame.image.load("C:/Users/hwonssam/workspace/nado_coding/pygame_bagic/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/hwonssam/workspace/nado_coding/pygame_bagic/character.png")
character_size = character.get_rect().size #이미지 크기를 구해옴
character_width = character_size[0] # 캐릭터 가로크기
character_height = character_size[1] #캐릭터 세로크기
character_x_pos = (screen_width-character_width) / 2 # 화면가로 절반에 위치
character_y_pos = screen_heingt - character_height  # 화면 세로 가장 아래 위치

#이동할 좌표
to_x = 0 

#이동속도
chracter_speed = 0.6 

#똥만들기
enemy = pygame.image.load("C:/Users/hwonssam/workspace/nado_coding/pygame_bagic/enemy.png")
enemy_size = enemy.get_rect().size #이미지 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터 가로크기
enemy_height = enemy_size[1] #캐릭터 세로크기
enemy_x_pos = random.randint(0,screen_width-enemy_width) # 화면가로 절반에 위치
enemy_y_pos = 0  # 화면 세로 가장 아래 위치
enemy_speed = 10

# 폰트 정의
game_font = pygame.font.Font(None, 60) #폰트 객체 생성(폰트,크기)

#총 시간
total_time = 30

#시간 정보
start_ticks = pygame.time.get_ticks() #시작 tick을 가져옴

#이벤트 루프
running = True
while running:
    dt = clock.tick(30) #게임화면의 초당프레임
    
    #2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False

        
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                to_x -=chracter_speed
            elif event.key == pygame.K_RIGHT :
                to_x +=chracter_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
    #3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos >screen_heingt:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0,screen_width-enemy_width)


    #4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
        
    #5. 화면에 그리기
    pygame.display.update() #게임화면 계속 그리기

    
    screen.blit(background, (0,0)) #배경그리기

    screen.blit(character, (character_x_pos,character_y_pos)) #캐릭터그리기

    screen.blit(enemy, (enemy_x_pos,enemy_y_pos)) #적그리기
#pygame 종료
pygame.quit()