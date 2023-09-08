import pygame 
import random 
import time 
clock = pygame.time.Clock()
pygame.init()

width, height = 400, 400
game_screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")


VEL_x , VEL_y = 10 ,0

def snake ():
    global x,y
    x =( x+ VEL_x)%width
    y= (y+ VEL_y)%height
    game_screen.fill((0, 0, 0))

    pygame.draw.rect(game_screen, (255,255,255), [x,y, 10,10])
    pygame.display.update()

    #move

x,y = 200, 200

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if VEL_x !=10:
                    VEL_x =-10
                VEL_y = 0
            elif event.key == pygame.K_RIGHT:
                if VEL_x!=-10:
                    VEL_x =10
                VEL_y= 0
            elif event.key == pygame.K_UP:
                if VEL_y!=10:
                    VEL_y= -10
                VEL_x=0
                
            elif event.key == pygame.K_DOWN:
                if VEL_y != -10:
                    VEL_y=10
                VEL_x =0
                
            else:
                continue
            snake()
    if not events:
        snake()
    clock.tick(10) 

                
    
