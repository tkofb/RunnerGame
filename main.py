from sys import exit
from random import randint
import pygame as p

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
timeEnded = 0
count = 0

def obstacleMovement(obstacleRectList):
    if obstacleRectList:
        for obstacleRect in obstacleRectList:
            obstacleRect.x -= 5
            
            if(obstacleRect.bottom == 300):
                screen.blit(snailSurface, obstacleRect)
            else:
                screen.blit(flySurface, obstacleRect)
        
        obstacleRectList = [i for i in obstacleRectList if i.x > -150]
        
        return obstacleRectList
    else:
        return []
    
def collisions(player, obstacles):
    if obstacles:
        for obstacleRect in obstacles:
            if player.colliderect(obstacleRect):
                return False

    return True

snail_x_pos = 800
snailSurface = p.image.load('RunnerGame/graphics/snail/snail1.png').convert_alpha()

flySurface = p.image.load('RunnerGame/graphics/Fly/Fly1.png').convert_alpha()

obstacleRectList = []


playerSurface = p.image.load('RunnerGame/graphics/Player/player_walk_1.png').convert_alpha()
playerRect = playerSurface.get_rect(midbottom = (80,300))
playerGravity = 0

playerOnFloor = True

playerEndGame = p.image.load('RunnerGame/graphics/Player/player_stand.png').convert_alpha()
playerEndGameScaled = p.transform.scale2x(playerEndGame)
playerEndGameRect = playerEndGameScaled.get_rect(center = (400,200))

    #Timer
obstacleTimer = p.USEREVENT + 1
p.time.set_timer(obstacleTimer,1400)
    


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
        if event.type == obstacleTimer and gameRunning:
            if randint(0,2) == 0:
                obstacleRectList.append(snailSurface.get_rect(bottomright = (randint(900,1100),300)))
            else:
                obstacleRectList.append(flySurface.get_rect(bottomright = (randint(900,1100),210)))

    if(gameRunning):
        
        #Puts one surface on the display surface
        screen.blit(skySurface,(0,0))
        screen.blit(groundSurface, (0,300))
        count = p.time.get_ticks() - timeEnded
        scoreSurface = font.render(f'Score: {round(count/1000)}', False, 'Green')
        scoreRectangle = scoreSurface.get_rect(midbottom = (400,80))
        screen.blit(scoreSurface, scoreRectangle)
        
        screen.blit(playerSurface,playerRect)
            

        playerGravity += 1
        playerRect.y += playerGravity

        if(playerRect.bottom >= 300):
            playerRect.bottom = 300

            
        if playerRect.bottom == 300:
            playerOnFloor = True
        else:
            playerOnFloor = False    
            
        obstacleRectList = obstacleMovement(obstacleRectList)
            
        gameRunning = collisions(playerRect, obstacleRectList)
        

    else:
        snail_x_pos = 800
        screen.fill((94,129,162))
        timeEnded = p.time.get_ticks()
        obstacleRectList.clear()
        playerRect.midbottom = (80,300)
        
        screen.blit(playerEndGameScaled,playerEndGameRect)
        scoreSurface = font.render(f'Score: {round(count/1000)}', False, 'Green')
        scoreRectangle = scoreSurface.get_rect(midbottom = (400,80))
        screen.blit(scoreSurface, scoreRectangle)

        instructionsSurface = font.render(f'Press Space to Play Again', False, 'Green')
        instructionsRectangle = instructionsSurface.get_rect(midbottom = (400,360))
        screen.blit(instructionsSurface, instructionsRectangle)
        
        
    



    p.display.update()
    clock.tick(60)
    
    
    
    


