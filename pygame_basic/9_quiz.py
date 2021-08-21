import pygame
import random

#################################################################
# 초기화
pygame.init() 

# 화면 크기
screen_width=480
screen_height=640
screen=pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀
pygame.display.set_caption("지브리") 

# fps
clock=pygame.time.Clock()

#################################################################

#  1. 사용자 게임 초기화(배경화면 게임 이미지, 좌표, 속도, 폰트)
# 배경화면
background=pygame.image.load("C:\\Users\\Seon\\Desktop\\project1_pygame_basic\\background.png")

# 캐릭터
character=pygame.image.load("C:\\Users\\Seon\\Desktop\\project1_pygame_basic\\character.png")
# 캐릭터 사이즈 부르기
character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
# 캐릭터 좌표
character_x_pos=(screen_width-character_width)/2
character_y_pos=screen_height-character_height

to_x=0
to_y=0
character_speed=0.6


# 적 캐릭터
enemy=pygame.image.load("C:\\Users\\Seon\\Desktop\\project1_pygame_basic\\smallEnemy.png")
enemy_size=enemy.get_rect().size
enemy_width=enemy_size[0]
enemy_height=enemy_size[1]
enemy_x_pos=random.randrange(0,int(screen_width-enemy_width))
enemy_y_pos=0
enemy_speed=10



# 이벤트 루프
running=True
while running:
    # 초당 프레임 수 설정
    dt=clock.tick(30)

    # 2. 이벤트 처리(키보드,마우스)
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            running=False
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                to_x-=character_speed
            elif event.key==pygame.K_RIGHT:
                to_x+=character_speed
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or pygame.K_RIGHT:
                to_x=0       

    # 3. 게임 캐릭터 위치 정의 

    character_x_pos+=to_x*dt
    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width

    if enemy_y_pos>screen_height:
        enemy_x_pos=random.randrange(0,int(screen_width-enemy_width))
        enemy_y_pos=0
    enemy_y_pos+=enemy_speed

       

    # 4. 충돌처리
    character_rect=character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos

    enemy_rect=character.get_rect()
    enemy_rect.left=enemy_x_pos
    enemy_rect.top=enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        running=False
    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    


    pygame.display.update()

pygame.time.delay(1000)
pygame.quit()