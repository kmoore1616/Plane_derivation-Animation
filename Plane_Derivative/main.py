import pygame
import math
import time
pygame.init()
width = 500
height = 375
win = pygame.display.set_mode((500, 375))
run = True

#Global Variables
x = 25
y = 25
find_x = 0
find_z = 0
text_x = str(find_x)
text_y = "1000"
text_z = str(find_z)
vel = 10

# Math Variables
math_x = 0
times = 0
dx = 708.185
velocity = 553
z = 0
start = time.time()
mathing = True

while run:
    # Setup for pygame
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Detects keypresses
    keys = pygame.key.get_pressed()
    
    if mathing:
        # Math
        ## Finds length of x
        times = round((start - time.time()), 2) * -1
        find_x = round(times * velocity, 2)

        ## Finds length of z
        find_z = round((1416.37 * (553 * times)) / 1106, 3)
    
    #Movement stuff
    if x <= 450:
        x += vel
    else:
        vel = 0
        mathing = False
        if keys[pygame.K_SPACE]:
            x = 25
            vel = 10
            start = time.time()
            mathing = True
            
    # Background color
    win.fill((102, 102, 255))
    
    # Shapes
    # Active Objects
    pygame.draw.rect(win, (95, 104, 106), (x, y, 50, 25))
    ## Z
    pygame.draw.line(win, (231, 24, 55), (60, 330), (x + 30, y + 10), 3)
    # Static Objects
    ## Y
    pygame.draw.line(win, (165, 214, 16), (60, y + 10), (x + 25, y + 10), 3)
    ## X
    pygame.draw.line(win, (165, 214, 16), (60, 340), (60, y + 10), 3)
    pygame.draw.rect(win, (0, 82, 53), (0, 325, 500, 50))
    pygame.draw.polygon(win, (0, 0, 0), ((50, 315), (50, 340), (70, 340), (70, 315)))
    pygame.draw.rect(win, (161, 164,163), (width - 100, height - 100, 65, 75))
    pygame.draw.rect(win, (255, 255,255), (width - 100, height - 100, 65, 75), 2)
    #Text
    ## XYZ lines
    font = pygame.font.SysFont(None, 30)
    img = font.render(text_y, True, (0, 0, 0))
    win.blit(img, (10, 180))
    
    img = font.render(text_x, True, (0, 0, 0))
    win.blit(img, ((width/2 - 30), 6))
    
    
    img = font.render(text_z, True, (0, 0, 0))
    win.blit(img, (((x/2) + 55), (height/2)))
    
    ## Speed Key
    font = pygame.font.SysFont(None, 15)
    img = font.render("V = 248 m/s", True, (0, 0 ,0))
    win.blit(img, (width-96, height-90))
    img = font.render("y = 1000m", True, (0, 0 ,0))
    win.blit(img, (width-96, height-75))
    img = font.render(f"x = {text_x}", True, (0, 0 ,0))
    win.blit(img, (width-96, height-60))
    img = font.render(f"z = {text_z}", True, (0, 0 ,0))
    win.blit(img, (width-96, height-45))
    
    
    text_x = str(find_x)
    text_z = str(find_z)
    pygame.display.flip()

pygame.quit()