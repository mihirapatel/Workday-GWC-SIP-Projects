import pygame, random, time

darkSalmon = (233,150,122)	
salmon = (250,128,114)		 
lightSalmon	= (255,160,122)	 
orange = (255,165,0)		 
darkOrange = (255,140,0)		 
coral = (255,127,80)		 
lightCoral = (240,128,128)	 
tomato = (255,99,71)		 
orangeRed = (255,69,0)

WHITE = (255, 255, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Scavenger")

pygame.mouse.set_visible(True)

pygame.init()

screen.fill(WHITE)

circleColors = [darkSalmon, salmon, lightSalmon, orange, darkOrange, coral,lightCoral, tomato, orangeRed]

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type ==pygame.MOUSEBUTTONDOWN:
            print ("Here")
            position = pygame.mouse.get_pos()
            
            radius = random.randint(25, 40)
            color = random.choice(circleColors)
            pygame.draw.circle(screen, color, position, radius)
        
    pygame.display.flip()
    

    
time.sleep(5)