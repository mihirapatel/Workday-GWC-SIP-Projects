"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)





pygame.init()




# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


possible_ball_colors = [BLACK, WHITE, GREEN, RED, BLUE, GREY]



x_speed = random.randint(-10, 10)
y_speed = random.randint(-10, 10)

x_location = int(SCREEN_WIDTH/2)
y_location = int(SCREEN_HEIGHT/2)

x2_speed = random.randint(-10, 10)
y2_speed = random.randint(-10, 10)

x2_location = int(SCREEN_WIDTH/2)
y2_location = int(SCREEN_HEIGHT/2)

x3_speed = random.randint(-10, 10)
y3_speed = random.randint(-10, 10)

x3_location = int(SCREEN_WIDTH/2)
y3_location = int(SCREEN_HEIGHT/2)

ball_size = random.randint(10, 30)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN)

    # --- Drawing code should go here

    ball_color = random.choice(possible_ball_colors) # This is outside because of variable scoping.

# 	BALL ONE

    pygame.draw.circle(screen, ball_color, [x_location, y_location], ball_size)
	
    if x_location >= SCREEN_WIDTH - ball_size or x_location < ball_size:
        x_speed = x_speed * -1

    if y_location >= SCREEN_HEIGHT - ball_size or y_location < ball_size:
        y_speed = y_speed * -1


    x_location += x_speed
    y_location += y_speed
    
    
    
#     BALL TWO

    pygame.draw.circle(screen, ball_color, [x2_location, y2_location], ball_size)
	
    if x2_location >= SCREEN_WIDTH - ball_size or x2_location < ball_size:
        x2_speed = x2_speed * -1

    if y2_location >= SCREEN_HEIGHT - ball_size or y2_location < ball_size:
        y2_speed = y2_speed * -1


    x2_location += x2_speed
    y2_location += y2_speed



# 	BALL THREE

    pygame.draw.circle(screen, ball_color, [x3_location, y3_location], ball_size)
	
    if x3_location >= SCREEN_WIDTH - ball_size or x3_location < ball_size:
        x3_speed = x3_speed * -1

    if y3_location >= SCREEN_HEIGHT - ball_size or y3_location < ball_size:
        y3_speed = y3_speed * -1


    x3_location += x3_speed
    y3_location += y3_speed

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
