import pygame
import os
pygame.mixer.init()
MAX_BULLETS = 3
BULLET_VEL = 7
RED = (255, 0, 0)
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 1200, 800
FPS = 60 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
SPACESHIP_WIDTH= 55
SPACESHIP_HEIGHT= 70
VEL = 5
YELLOW = (255, 255, 0)
BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')
RED_HIT = pygame.USEREVENT + 2
YELLOW_HIT = pygame.USEREVENT + 1
yellow_spaceship_image= pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
yellow_spaceship_scaled = pygame.transform.scale(yellow_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
yellow_spaceship= pygame.transform.rotate(yellow_spaceship_scaled, 90)

purple_spaceship_image= pygame.image.load(os.path.join('Assets', 'spaceship_purple.png'))
purple_spaceship = pygame.transform.scale(purple_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))


red_spaceship_image= pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
red_spaceship_scaled = pygame.transform.scale(red_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
red_spaceship = pygame.transform.rotate(red_spaceship_scaled, 270)



def draw_window(red, yellow, purple, red_bullets, yellow_bullets):
    WIN.fill(WHITE)
    WIN.blit(yellow_spaceship, (yellow.x, yellow.y))
    WIN.blit(red_spaceship, (red.x, red.y))
    WIN.blit(purple_spaceship, (purple.x, purple.y))
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)


        

    pygame.display.update()


def purple_handle_movement(keys_pressed, purple):
     if keys_pressed[pygame.K_f] and purple.x - VEL >0 : #LEFT
        purple.x -= VEL
     if keys_pressed[pygame.K_h] and purple.x + VEL  < 450:  # RIGHT
        purple.x += VEL
     if keys_pressed[pygame.K_t] and purple.y - VEL >0: #UP
        purple.y-= VEL
     if keys_pressed[pygame.K_g] and purple.y + VEL + purple.height < HEIGHT - 15:  # DOWN
        purple.y += VEL
    

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL >0 :
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL  < 450:  
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: 
        yellow.y += VEL

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > 0:
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width > 0:  
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height > 0: 
        red.y += VEL
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def main():
    red = pygame.Rect(600, 100, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    purple = pygame.Rect (200, 600, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(200, 100, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow_bullets = []
    red_bullets = []
    clock = pygame.time.Clock()
    run = True
    while run:
        
       
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                    yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 10)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
        
        keys_pressed = pygame.key.get_pressed()
        draw_window(red, yellow, purple, red_bullets, yellow)
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        purple_handle_movement(keys_pressed, purple)
    main()

if __name__  == "__main__":
    main()
