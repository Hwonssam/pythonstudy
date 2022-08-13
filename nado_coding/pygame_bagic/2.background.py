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

#이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
    #screen.fill((0,0,255))
    screen.blit(background, (0,0)) #배경그리기

    pygame.display.update()
#pygame 종료
pygame.quit()