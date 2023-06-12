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

count = p.time.get_ticks
scoreSurface = font.render(f'Score: {count}', False, 'Green')
scoreRectangle = scoreSurface.get_rect(midbottom = (400,50))

snail_x_pos = 800

snailSurface = p.image.load('RunnerGame/graphics/snail/snail1.png').convert_alpha()

#Animates the movement of the snail


playerSurface = p.image.load('RunnerGame/graphics/Player/player_walk_1.png').convert_alpha()
playerRect = playerSurface.get_rect(midbottom = (80,300))
playerGravity = 0

playerOnFloor = True

while True:
    #Quits the game when it is running
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            exit()

        if gameRunning:   
            if event.type == p.KEYDOWN and playerOnFloor:
                if event.key == p.K_UP or event.key == p.K_SPACE :
                    playerGravity = -20
        else:
            if event.type == p.KEYDOWN:
                if event.key == p.K_UP or event.key == p.K_SPACE :
                    gameRunning = True
    
    if(gameRunning):
        snailRect = snailSurface.get_rect(midbottom = (snail_x_pos,300))
        #Puts one surface on the display surface
        screen.blit(skySurface,(0,0))
        screen.blit(groundSurface, (0,300))
        screen.blit(scoreSurface, scoreRectangle)
        screen.blit(snailSurface, snailRect)
        screen.blit(playerSurface,playerRect)
            

        playerGravity += 1
        playerRect.y += playerGravity

            

        if(snail_x_pos == -100):
            snail_x_pos = 800
                
        snail_x_pos -= 2

        if(playerRect.bottom >= 300):
            playerRect.bottom = 300

            
        if playerRect.bottom == 300:
            playerOnFloor = True
        else:
            playerOnFloor = False    
            
        if(snailRect.colliderect(playerRect)):
            gameRunning = False
    else:
        snail_x_pos = 800
        screen.fill('yellow')
   



    p.display.update()
    clock.tick(60)
