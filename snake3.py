import pygame
import random
import time
clock = pygame.time.Clock()
pygame.init()
width, height = 400, 400

game_screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("snake")
x,y = 200, 200
VEL_x , VEL_y = 10 ,0
body_list = [(x,y)]
food_x, food_y = random.randrange(0, width)//10*10, random.randrange(0, height)//10*10

game_over=False

def snake ():
    global x,y, food_x, food_y
    x =( x+ VEL_x)%width
    y= (y+ VEL_y)%height

    
    body_list.append((x,y))

     
    if (food_x == x and food_y == y):
        while((food_x,food_y) in body_list):
            food_x, food_y = random.randrange(0,width)//10*10, random.randrange(0,height)//10*10
    else:
        del body_list[0]

    game_screen.fill((0,200,0))

    #increase length of a snake
    for(i,j ) in body_list:
        pygame.draw.rect(game_screen, (0,0,255), [i,j, 12,12])
    #drawing food
    pygame.draw.rect(game_screen,(255,0,0), [food_x,food_y, 12,12])
    pygame.display.update()


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