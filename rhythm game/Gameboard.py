from globvar import *
from utilities import load, map_load,drawSquares
from game_objects import player_object, Bullet
from game_actions import key_interact, player, asteroid_movement, map_info, bullets,shootCheck

x = 0


def gameLoop():
    global player
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    global x
    for asteroid in map_info:
        x+=1
        
        check = player.collision(asteroid)
        if check == True:
            return False
        for bullet in bullets:
            check = bullet.collision(asteroid)
            if check:
                map_info.remove(asteroid)
                bullets.remove(bullet)
    key_interact(player.position)
    shootCheck()
    screen.fill((25,25,25))
    
    pygame.draw.rect(screen,cColor,cSquare)
    drawSquares()
    player.draw(screen)
    #asteroid_movement()
    for bullet in bullets:
        bullet.colorChange()
    pygame.display.update()
    return True
check = True
while check:
    check = gameLoop()
    clock.tick(60)