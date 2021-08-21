import os
import pygame

#################################################################
# 초기화
pygame.init() 

# 화면 크기
screen_width=640    
screen_height=480
screen=pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀
pygame.display.set_caption("Pang") 

# fps
clock=pygame.time.Clock()

#################################################################

#  1. 사용자 게임 초기화(배경화면 게임 이미지, 좌표, 속도, 폰트)
current_path=os.path.dirname(__file__)
image_path=os.path.join(current_path,"images")
# 배경
background=pygame.image.load(os.path.join(image_path,"background.png"))
# 스테이지
stage=pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size=stage.get_rect().size
stage_height=stage_size[1]

# 캐릭터
character=pygame.image.load(os.path.join(image_path,"character.png"))
character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=(screen_width-character_width)/2
character_y_pos=screen_height-stage_height-character_height

# 이벤트 루프
running=True
while running:
    # 초당 프레임 수 설정
    dt=clock.tick(30)

    # 2. 이벤트 처리(키보드,마우스)
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            running=False
       
    # 3. 게임 캐릭터 위치 정의 

    # 4. 충돌처리
    
    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update()

pygame.quit()