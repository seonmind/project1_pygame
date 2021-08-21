import pygame

pygame.init() #초기화

# 화면 크기
screen_width=480
screen_height=640
screen=pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀
pygame.display.set_caption("The Game") 

# fps
clock=pygame.time.Clock()

# 배경 이미지 불러오기
background=pygame.image.load("C:\\Users\\Seon\\Desktop\\project1_pygame_basic\\background.png")

# 캐릭터(스프라이트 불러오기)
character=pygame.image.load('C:/Users/Seon/Desktop/project1_pygame_basic/character.png')
character_size=character.get_rect().size 
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=screen_width/2-character_width/2
character_y_pos=screen_height-character_height

# 캐릭터 이동 좌표
to_x=0
to_y=0

# 이동속도
character_speed=0.3


# 이벤트 루프
running=True
while running:
    # 초당 프레임 수 설정
    dt=clock.tick(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            running=False
        # 키가 눌러졌을 때
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                to_x-=character_speed
            elif event.key==pygame.K_RIGHT:
                to_x+=character_speed
            elif event.key==pygame.K_UP:
                to_y-=character_speed
            elif event.key==pygame.K_DOWN:
                to_y+=character_speed
        # 키를 땠을때
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or pygame.K_RIGHT:
                to_x=0
            elif event.key==pygame.K_UP or pygame.K_DOWN:
                to_y=0
    # 캐릭터 좌표 이동
    character_x_pos+=to_x*dt
    character_y_pos+=to_y*dt
    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos > screen_width-character_width:
        character_x_pos=screen_width-character_width
    if character_y_pos<0:
        character_y_pos=0
    elif character_y_pos>screen_height-character_height:
        character_y_pos=screen_height-character_height


    # 배경 그리기
    screen.blit(background,(0,0))
    # 캐릭터 그리기
    screen.blit(character,(character_x_pos,character_y_pos))
    # 화면 업데이트로 배경 표시
    pygame.display.update()

pygame.quit()