import pygame
from sys import exit

#Initializes pygame
pygame.init()
#Sets the display surface/window
screen = pygame.display.set_mode((800,400))
#Changes the name of the display
pygame.display.set_caption('Runner')
gameRunning = True
#Creates a clock object used for frame rates
clock = pygame.time.Clock()
#Creating a regular surface
skySurface = pygame.image.load('RunnerGame/graphics/Sky.png')
groundSurface = pygame.image.load('RunnerGame/graphics/ground.png')

while gameRunning:
    #Quits the game when it is running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Puts one surface on the display surface
    screen.blit(skySurface,(0,0))
    screen.blit(groundSurface, (0,300))
    pygame.display.update()
    clock.tick(60)
