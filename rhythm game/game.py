from menu import startMenu, levelSelect
from Gameboard import gameLoop
from globvar import *
loop = True
def test():
    return True
while loop:
    clock.tick(20)
    check = startMenu()
    if check == False:
        loop = False
loop = True

while True:
    clock.tick(60)
    gameLoop()
    