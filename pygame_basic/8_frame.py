import pygame

#################################################################
# 초기화
pygame.init() 

# 화면 크기
screen_width=480
screen_height=640
screen=pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀
pygame.display.set_caption("게임 이름") 

# fps
clock=pygame.time.Clock()

#################################################################

#  1. 사용자 게임 초기화(배경화면 게임 이미지, 좌표, 속도, 폰트)

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

    pygame.display.update()

pygame.quit()