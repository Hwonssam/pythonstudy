import pygame

pygame.init()
#화면크리
screen_width = 480
screen_heingt = 640
screen = pygame.display.set_mode((screen_width, screen_heingt))

#화면 타이틀
pygame.display.set_caption("Nado Game") #게임이름

#이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
#pygame 종료
pygame.quit()