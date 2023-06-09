import pygame
from sys import exit

#Initializes pygame
pygame.init()
screen = pygame.display.set_mode((800,400))
#Changes the name of the display
pygame.display.set_caption('Runner')
gameRunning = True
#Creates a clock object used for frame rates
clock = pygame.time.Clock()

while gameRunning:
    #Quits the game when it is running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
