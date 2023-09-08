import pygame

pygame.init()
width , height = 400, 400

game_window = pygame.display.set_mode((width , height))

x,y = 200, 200
VEL_x,VEL_y = 0,0
def snake():
    global x,y
    x = x + VEL_x
    y = y + VEL_y    
    pygame.draw.rect(game_window,(255, 0, 0), [x, y, 10, 10])
    pygame.display.update()
while True:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                VEL_x = -10
                VEL_y = 0
            elif event.key == pygame.K_RIGHT:
                VEL_x = 10
                VEL_y = 0
            elif event.key == pygame.K_UP:
                VEL_x = 0
                VEL_y = -10
            elif event.key == pygame.K_DOWN:
                VEL_x = 0
                VEL_y = 10
            else:
                continue
            snake()

       