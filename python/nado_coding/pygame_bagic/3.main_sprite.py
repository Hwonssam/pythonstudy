import pygame

pygame.init()
#화면크기
screen_width = 480
screen_heingt = 640
screen = pygame.display.set_mode((screen_width, screen_heingt))

#화면 타이틀
pygame.display.set_caption("Nado Game") #게임이름

#배경이미지 불러오기
background = pygame.image.load("C:/Users/hwonssam/workspace/nado_coding/pygame_bagic/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/hwonssam/workspace/nado_coding/pygame_bagic/character.png")
character_size = character.get_rect().size #이미지 크기를 구해옴
character_width = character_size[0] # 캐릭터 가로크기
character_height = character_size[1] #캐릭터 세로크기
character_x_pos = (screen_width-character_width) / 2 # 화면가로 절반에 위치
character_y_pos = screen_heingt - character_height  # 화면 세로 가장 아래 위치

#이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
    #screen.fill((0,0,255))
    screen.blit(background, (0,0)) #배경그리기

    screen.blit(character, (character_x_pos,character_y_pos)) #배경그리기


    pygame.display.update()
#pygame 종료
pygame.quit()