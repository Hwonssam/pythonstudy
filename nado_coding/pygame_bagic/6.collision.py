from email.utils import parseaddr
from msilib.schema import EventMapping
import pygame

pygame.init()
#화면크기
screen_width = 480
screen_heingt = 640
screen = pygame.display.set_mode((screen_width, screen_heingt))

#화면 타이틀
pygame.display.set_caption("Nado Game") #게임이름

# FPS
clock = pygame.time.Clock()


#배경이미지 불러오기
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
to_y = 0

#이동속도
chracter_speed = 0.6 

#적 enemy캐릭터
enemy = pygame.image.load("C:/Users/hwonssam/workspace/nado_coding/pygame_bagic/enemy.png")
enemy_size = enemy.get_rect().size #이미지 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터 가로크기
enemy_height = enemy_size[1] #캐릭터 세로크기
enemy_x_pos = (screen_width-enemy_width) / 2 # 화면가로 절반에 위치
enemy_y_pos = (screen_heingt - enemy_height) / 2  # 화면 세로 가장 아래 위치

#이벤트 루프
running = True
while running:
    dt = clock.tick(60) #게임화면의 초당프레임

#캐릭터가 100만큼 이동해야해
# 10 fps: 1초동안에 10번동작 -> 1번에 몇만큼 이동해야 100? 10만큼
# 20fps : 1초 동안에 20번 동작 -> 5만큼 이동해야함!

    print("fps : " + str(clock.get_fps()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
    #screen.fill((0,0,255))

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                to_x -=chracter_speed
            elif event.key == pygame.K_RIGHT :
                to_x +=chracter_speed
            elif event.key == pygame.K_UP :
                to_y -=chracter_speed
            elif event.key == pygame.K_DOWN :
                to_y +=chracter_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #가로, 세로 경계선 설정
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_heingt - character_height:
        character_y_pos = screen_heingt - character_height

    #충돌처리를 위한 reck 정보 업데이트
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

    screen.blit(background, (0,0)) #배경그리기

    screen.blit(character, (character_x_pos,character_y_pos)) #캐릭터그리기

    screen.blit(enemy, (enemy_x_pos,enemy_y_pos)) #적그리기



    pygame.display.update()
#pygame 종료
pygame.quit()