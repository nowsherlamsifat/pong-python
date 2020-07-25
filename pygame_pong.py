import pygame,sys,time

"""global variables"""
SCREEN_HEIGHT=600
SCREEN_WIDTH=800
PADDLE_HEIGHT=120
PADDLE_WIDTH=10
PADDLE_SPEED=10
BALL_SPEED=5
TURN=1
GAME_RUNNING=True
winning_score=int(input('winning score:'))

"""screen objects"""
pygame.init()

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('PONG')
bg_color=pygame.Color('grey12')
clock=pygame.time.Clock()

"""paddle A"""
paddle_A=pygame.Rect(50,int(SCREEN_HEIGHT/2)-70,PADDLE_WIDTH,PADDLE_HEIGHT)
paddle_A_color=pygame.Color('red2')
paddle_A_move=0
paddle_A_score=0

    
def paddle_A_movement():
    if paddle_A.y<10:
        paddle_A.y=10
    if paddle_A.y>SCREEN_HEIGHT-PADDLE_HEIGHT-20:
        paddle_A.y=SCREEN_HEIGHT-PADDLE_HEIGHT-20
    paddle_A.y+=paddle_A_move
    
    
"""paddle B"""
paddle_B=pygame.Rect(SCREEN_WIDTH-70,int(SCREEN_HEIGHT/2)-70,PADDLE_WIDTH,PADDLE_HEIGHT)
paddle_B_color=(0,0,255)
paddle_B_move=0
paddle_B_score=0

def paddle_B_movement():
    if paddle_B.y<10:
        paddle_B.y=10
    if paddle_B.y>SCREEN_HEIGHT-PADDLE_HEIGHT-20:
        paddle_B.y=SCREEN_HEIGHT-PADDLE_HEIGHT-20
    paddle_B.y+=paddle_B_move


"""ball"""
ball_width=20
ball_height=20
ball=pygame.Rect(int(SCREEN_WIDTH/2)-15,int(SCREEN_HEIGHT/2)-15,ball_width,ball_height)
ball_color=pygame.Color('yellow')
ball_DX=BALL_SPEED
ball_DY=BALL_SPEED
ball_hit_wall=False

def ball_movment():
    global ball_DX, ball_DY,ball_hit_wall,paddle_A_score,paddle_B_score
    
    """ball moving"""
    ball.x+=ball_DX
    ball.y+=ball_DY
        
    """ball hit left side"""
    if ball.x<0:
        ball_DX*=-1
        ball_DX=0
        ball_hit_wall=True
      
        """player1 ball set"""
        ball.x=paddle_A.x+10
        ball.y=paddle_A.y+int(PADDLE_HEIGHT/2)
        paddle_B_score+=paddle_A_score
        paddle_A_score=0
        
            
    if ball.x>SCREEN_WIDTH-ball_width:
        ball_DX*=-1
        ball_DX=0
        ball_hit_wall=True
        
        """player2 ball set"""
        ball.x=paddle_B.x-20
        ball.y=paddle_B.y+int(PADDLE_HEIGHT/2)
        paddle_A_score+=paddle_B_score
        paddle_B_score=0
        
        
    if ball.y<0:
        ball_DY*=-1
    if ball.y>SCREEN_HEIGHT-ball_height:
        ball_DY*=-1
    
    """ball moving infront of paddle"""
    if ball_hit_wall:
        """for paddle a"""
        if ball.x==paddle_A.x+10:
            if ball.y>paddle_A.y+PADDLE_HEIGHT-20:
                ball_DY*=-1
            
            if ball.y<paddle_A.y:
                ball_DY*=-1
            
        """for paddle b"""
        if ball.x==paddle_B.x-20:
            if ball.y>paddle_B.y+PADDLE_HEIGHT-20:
                ball_DY*=-1
            
            if ball.y<paddle_B.y:
                ball_DY*=-1
    
        
    """ball paddle collide"""
    if ball.x>paddle_A.x-10 and ball.x<paddle_A.x and ball.y<paddle_A.y+PADDLE_HEIGHT and ball.y>paddle_A.y:
        ball_DX*=-1
        paddle_A_score+=1
        
    if ball.x<paddle_B.x and ball.x>paddle_B.x-10 and ball.y<paddle_B.y+PADDLE_HEIGHT and ball.y>paddle_B.y:
        ball_DX*=-1
        paddle_B_score+=1

"""drawing object"""
def draw_all():
    pygame.draw.rect(screen,paddle_A_color,paddle_A)#red paddle
    pygame.draw.rect(screen,paddle_B_color,paddle_B)#blue paddle
    pygame.draw.ellipse(screen,ball_color,ball)#ball
    pygame.draw.rect(screen,(255,255,255),(int(SCREEN_WIDTH/2)-10,0,10,SCREEN_HEIGHT))#divide line
    
def show_score():
    text=pygame.font.SysFont('comicsansms',23)
    paddle1=text.render(f'{paddle_A_score}',True,paddle_A_color)
    screen.blit(paddle1,(paddle_A.x-40,paddle_A.y+50))
        
    paddle2=text.render(f'{paddle_B_score}',True,paddle_B_color)
    screen.blit(paddle2,(paddle_B.x+40,paddle_B.y+50))

def show_winner():
    global GAME_RUNNING
    
    text=pygame.font.Font('freesansbold.ttf',60)
    
    if paddle_A_score>=winning_score:
        winner=text.render('PLAYER RED WINS',True,paddle_A_color)
        screen.blit(winner,(150,300))
        GAME_RUNNING=False
        
    elif paddle_B_score>=winning_score:
        winner=text.render('PLAYER BLUE WINS',True,paddle_B_color)
        screen.blit(winner,(150,300))
        GAME_RUNNING=False
        
while True:
    screen.fill(bg_color)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            
        if event.type==pygame.MOUSEBUTTONDOWN:
            y=event.pos[1]
            print(y)
            
        if event.type==pygame.KEYDOWN:

            """paddle a key"""
            if event.key==pygame.K_w:
                if not ball_hit_wall:
                    paddle_A_move=-PADDLE_SPEED
                    
            if event.key==pygame.K_s:
                if not ball_hit_wall:
                    paddle_A_move=PADDLE_SPEED
            
            """paddle b key"""
            if event.key==pygame.K_UP:
                if not ball_hit_wall:
                    paddle_B_move=-PADDLE_SPEED
                    
            if event.key==pygame.K_DOWN:
                if not ball_hit_wall:
                    paddle_B_move=PADDLE_SPEED
                
            if event.key==pygame.K_SPACE:
                if TURN==1:
                    if ball_hit_wall:
                        ball_DX=BALL_SPEED
                        ball_hit_wall=False
                else:
                    if ball_hit_wall:
                        ball_DX=-BALL_SPEED
                        ball_hit_wall=False
                    
                TURN+=1
                TURN%=2
                        
                
        if event.type==pygame.KEYUP:
            paddle_A_move=0
            paddle_B_move=0
    
    
        
    draw_all()
    paddle_A_movement()
    paddle_B_movement()
    ball_movment()
    
    show_score()
    show_winner()
    
    clock.tick(100)
    pygame.display.update()

    if not GAME_RUNNING:
        time.sleep(3)
        sys.exit()
