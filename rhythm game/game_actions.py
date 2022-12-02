from globvar import *
from utilities import map_load
from game_objects import player_object
bullets=[]
player = player_object((350,350),bullets.append)
map_info = map_load("BoogieWonderland")

def key_interact(position):
    global aHeld, wHeld, sHeld, dHeld, player

    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_RIGHT]:
        player.speen(1)
    elif key_pressed[pygame.K_LEFT]:
        player.speen(3)
    elif key_pressed[pygame.K_UP]:
        player.speen(2)
    elif key_pressed[pygame.K_DOWN]:
        player.speen(0)
    
    if key_pressed[pygame.K_a]:
        if not aHeld:
            player.altMove(1)
        aHeld = True
    else:
        aHeld = False

    if key_pressed[pygame.K_w]:
        if not wHeld:
            player.altMove(2)
        wHeld = True
    else:
        wHeld = False

    if key_pressed[pygame.K_d]:
        if not dHeld:
            player.altMove(3)
        dHeld = True
    else:
        dHeld = False

    if key_pressed[pygame.K_s]:
        if not sHeld:
            player.altMove(4)
        sHeld = True
    else:
        sHeld = False
def shootCheck():
    global spaceHeld
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_SPACE]:
        if not spaceHeld:
            player.shoot()
        spaceHeld = True
    else:
        spaceHeld = False

def asteroid_movement():
    for asteroid in map_info:
        asteroid.draw(screen)
        asteroid.move()
        test=0
        track = asteroid.move()
        if track > width + 100:
            map_info.remove(asteroid)
    if len(map_info) <= 0:
        pygame.quit()
        quit() #eventually make this return a boolean for whether or not map is done to end the gameloop process/do menu stuff
