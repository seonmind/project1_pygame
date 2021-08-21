import pygame

pygame.init() #초기화

# 화면 크기
screen_width=480
screen_height=640
screen=pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀
pygame.display.set_caption("The Game") 

# 배경 이미지 불러오기
background=pygame.image.load("C:\\Users\\Seon\\Desktop\\pygame_basic\\background.png")

# 캐릭터(스프라이트 불러오기)
character=pygame.image.load('C:/Users/Seon/Desktop/pygame_basic/character.png')
character_size=character.get_rect().size 
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=screen_width/2-character_width/2
character_y_pos=screen_height-character_height



# 이벤트 루프
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            running=False
    # 배경 그리기
    screen.blit(background,(0,0))
    # 캐릭터 그리기
    screen.blit(character,(character_x_pos,character_y_pos))
    # 화면 업데이트로 배경 표시
    pygame.display.update()

pygame.quit()