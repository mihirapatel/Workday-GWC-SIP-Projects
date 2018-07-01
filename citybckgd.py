import pygame
import random
from city_scroller import Scroller 


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.init()

pygame.display.set_caption("Runner Game")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)



FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)

front_scroller = Scroller(800, 400, 600, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(800, 200, (600 - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(800, 20, (600 - 100), BACK_SCROLLER_COLOR, 1)




# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Runner Sprite
class RunnerSprite (pygame.sprite.Sprite):
    # constructor with parameters for color, widt, height
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self. height = height
      # call arent class
        pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

    def draw(self):
        pygame.draw.rect(screen, self.color, (350, 250, self.width, self.height))

    def move(self):
        (xCor, yCor) = pygame.mouse.get_pos()
        self.rect.center = (xCor, yCor)


runner_1 = RunnerSprite(MIDDLE_SCROLLER_COLOR, 50, 50)
add_sprites_list = pygame.sprite.Group()
add_sprites_list.add(runner_1)

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
    screen.fill(BACKGROUND_COLOR)

    # --- Drawing code should go here
    back_scroller.draw_buildings()
    back_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    front_scroller.draw_buildings()
    front_scroller.move_buildings()
    runner_1.draw()
    


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
