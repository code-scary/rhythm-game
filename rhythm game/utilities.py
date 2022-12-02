from globvar import *
from game_objects import asteroids

class levelInfo():
    def __init__(self, levelName, levelFile, bpm):
        self.levelName = levelName
        self.levelFile = levelFile
        self.bpm = bpm

class subC():
    def __init__(self, position, width):
        self.x = position[0]
        self.y = position[1]
        self.width = width
        self.rect = pygame.Rect(self.x,self.y,self.width,self.width)
subCS = [
    subC((cX,cY), subCWidth),
    subC((cX+subCWidth,cY), subCWidth),
    subC((cX+(subCWidth*2),cY), subCWidth),
    
    subC((cX,cY+subCWidth), subCWidth),
    subC((cX+subCWidth,cY+subCWidth), subCWidth),
    subC((cX+(subCWidth*2),cY+subCWidth), subCWidth),

    subC((cX,cY+(subCWidth*2)), subCWidth),
    subC((cX+subCWidth,cY+(subCWidth*2)), subCWidth),
    subC((cX+(subCWidth*2),cY+(subCWidth*2)), subCWidth),
    
]
def map_load(map):
    asters = []
    directions = []
    mixer.music.load(map+".mp3")
    #mixer.music.play()
    f = open("BoogieWonderland.txt", "r")
    data=f.readlines()
    for line in range(len(data)):
        for x in range(len(data[line])):
            if data[line][x]=='0':
                if x == 0:
                    """"pos = random.randint(1,3)"""
                    pos = 1
                    if pos == 1:
                        pos = 50
                    elif pos == 2:
                        pos = -50
                    elif pos == 3:
                        pos = 0
                    asters.append(asteroids((0-25,screen.get_rect().centery+pos),line,0))
                if x == 1:
                    pos = random.randint(1,3)
                    if pos == 1:
                        pos = 50
                    elif pos == 2:
                        pos = -50
                    elif pos == 3:
                        pos = 0
                    asters.append(asteroids((screen.get_rect().centerx+pos,0-25),line,1))
                if x == 2:
                    pos = random.randint(1,3)
                    if pos == 1:
                        pos = 50
                    elif pos == 2:
                        pos = -50
                    elif pos == 3:
                        pos = 0
                    asters.append(asteroids((width+25,screen.get_rect().centery+pos),line,2))
                if x == 3:
                    pos = random.randint(1,3)
                    if pos == 1:
                        pos = 50
                    elif pos == 2:
                        pos = -50
                    elif pos == 3:
                        pos = 0
                    asters.append(asteroids((screen.get_rect().centerx+pos,height+25),line,3))
    return asters
def drawSquares():
    for square in subCS:
        pygame.draw.rect(screen, subCColor,square.rect, 1)
