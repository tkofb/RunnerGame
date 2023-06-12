import pygame as p
from sys import exit

#Initializes pygame
p.init()
#Sets the display surface/window
screen = p.display.set_mode((800,400))
#Changes the name of the display
p.display.set_caption('Runner')
gameRunning = True
#Creates the font used in the program
font = p.font.Font('RunnerGame/font/Pixeltype.ttf', 50)
#Creates a clock object used for frame rates
clock = p.time.Clock()
#Creating a regular surface
skySurface = p.image.load('RunnerGame/graphics/Sky.png').convert()
groundSurface = p.image.load('RunnerGame/graphics/ground.png').convert()
textSurface = font.render('My game', False, 'Green')

snail_x_pos = 800

snailSurface = p.image.load('RunnerGame/graphics/snail/snail1.png').convert_alpha()

#Animates the movement of the snail


playerSurface = p.image.load('RunnerGame/graphics/Player/player_walk_1.png').convert_alpha()
playerRect = playerSurface.get_rect(midbottom = (80,300))

while gameRunning:
    #Quits the game when it is running
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            exit()

    snailRect = snailSurface.get_rect(midbottom = (snail_x_pos,300))
    #Puts one surface on the display surface
    screen.blit(skySurface,(0,0))
    screen.blit(groundSurface, (0,300))
    screen.blit(textSurface, (300,50))
    screen.blit(snailSurface, snailRect)
    screen.blit(playerSurface,playerRect)



    if(snail_x_pos == -100):
        snail_x_pos = 800
    snail_x_pos -= 2


    #Updates the screens and sets the fps
    p.display.update()
    clock.tick(60)
