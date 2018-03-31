import pygame
import pygame.mixer
from pygame.locals import *
import random
import sys
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()
# Set the width and height of the screen [width, height]
size = (850, 600)
image_x_coordinate = 20
image_y_coordinate = 340
Rapper = ['gucci.png','21.png', 'djkhaled.png','desiigner.png','liljohn.png']
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Whack-A-Rapper")
chosen_rapper = random.choice(Rapper)

image_of_rapper = pygame.image.load(chosen_rapper).convert()
image_of_rapper = pygame.transform.scale(image_of_rapper,(120,200))
# Loop until the user clicks the close button.
running = True
# Used to manage how fast the screen updates
fpsClock = pygame.time.Clock()
clock = pygame.time.Clock()
img_width = 120
img_height = 200
background_image = pygame.image.load("mole_cover.jpg").convert()
background_image = pygame.transform.scale(background_image, size)
Img = pygame.image.load(chosen_rapper).convert()
Img = pygame.transform.scale(Img, (img_width,img_height))
rise = 'yes'
Holes = [(20,210),(100,300)]
steps = 3
ready_for_nxt_img=False
not_whacked = True
lower_y_limit = 220
upper_y_limit = 340
# -------- Main Program Loop -----------
while (running):
    if ready_for_nxt_img:
        screen.blit(Img, [random.choice(Holes)])
    if rise == 'yes':
        image_y_coordinate -= steps
        if image_y_coordinate <= lower_y_limit:
            rise = 'no'
    elif rise == 'no':
        image_y_coordinate += steps
        if image_y_coordinate >= upper_y_limit:
            rise = ' '
            ready_for_nxt_img = True
    else:
        pass

    screen.blit(background_image, [0, 0])
    if not_whacked:
        screen.blit(image_of_rapper, [image_x_coordinate, image_y_coordinate])
    else:
        ready_for_nxt_img = True
    
    # --- Main event loop
    cur = pygame.mouse.get_pos()  # taking click events every time
    click = pygame.mouse.get_pressed()  # again, every time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            click_on_picture = (((x >= image_x_coordinate) and 
            (x<image_x_coordinate+img_width)) and ((y >= image_y_coordinate) and 
            (y<image_y_coordinate+img_height)))

            if click_on_picture:
                not_whacked = False
    #if click[0] == 1: 

        

    # --- Game logic should go
    # --- Game logic should go here
    


    # --- Drawing code should go here
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(60)
    # --- Limit to 10 frames per second
    fpsClock.tick(10)
    
