from globvar import *
from utilities import levelInfo

font = pygame.font.Font('piano_keys_correct.ttf',200)
comic = pygame.font.Font("Qdbettercomicsans-jEEeG.ttf" , 30)
class Menu_Buttons():
    def __init__(self,x, y, color1, color2, text):
        self.x=x
        self.y=y
        self.color1=color1
        self.color2=color2
        self.text = text
        self.width = 200
        self.height =50
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)

menuButtons = [
    Menu_Buttons(width/2-100,380,color_light,color_dark, "Start"),
    Menu_Buttons(width/2-100,440,color_light,color_dark, "Options"),
    Menu_Buttons(width/2-100,500,color_light,color_dark,"Quit")
]

levels = [
    levelInfo("Boogie Wonderland", "BoogieWonderland",132 ),
    levelInfo("cheese","cheese", 60),
    levelInfo("cheese","cheese", 60),
    levelInfo("cheeeeese","cheese", 60),
    levelInfo("cese","cheese", 60),
    levelInfo("che","cheese", 60),
    levelInfo("eeeeeeeeeeeee","cheese", 60),
]

levelButtons = []
tempY=100
for level in levels:
    #figure out how to only load some of them
    #rect.move maybe? and compare to the height of the screen?
    #with a blank list for loaded rects, and we add/delete them from the secondary list as we scroll
    levelButtons.append(Menu_Buttons(width/2-100, tempY, color_light, color_dark, level.levelName))
print(levelButtons)


def startMenu():
  screen.fill((0, 0, 0))
  for button in menuButtons:
    pygame.draw.rect(screen, button.color1,button.rect,2)
    comicObj = comic.render(button.text,True,(255,255,255))
    comicRect = comicObj.get_rect(topleft = (button.x,button.y))
    comicRect = comicRect.move(button.width/2-(comicRect.width/2),button.height/2-(comicRect.height/2))
    screen.blit(comicObj,comicRect)
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit()

        if ev.type == pygame.MOUSEBUTTONDOWN: 
            mouse = pygame.mouse.get_pos()
            quitButton = menuButtons[2]
            startButton = menuButtons[0]
            if quitButton.x <= mouse[0] <= quitButton.x+quitButton.width and quitButton.y <= mouse[1] <= quitButton.y+quitButton.height: 
                pygame.quit() 
                sys.exit()
            if startButton.x <= mouse[0] <= startButton.x+startButton.width and startButton.y <= mouse[1] <= startButton.y+startButton.height:
                return False
  mouse = pygame.mouse.get_pos()
  startButton = menuButtons[0]
  optionButton = menuButtons[1]
  quitButton = menuButtons[2]

  if quitButton.x <= mouse[0] <= quitButton.x+quitButton.width and quitButton.y <= mouse[1] <= quitButton.y+quitButton.height: 
    pygame.draw.rect(screen,quitButton.color2,quitButton.rect,2)
  if startButton.x <= mouse[0] <= startButton.x+startButton.width and startButton.y <= mouse[1] <= startButton.y+startButton.height:
     pygame.draw.rect(screen,startButton.color2,startButton.rect,2)
  if optionButton.x <= mouse[0] <= optionButton.x+optionButton.width and optionButton.y <= mouse[1] <= optionButton.y+optionButton.height:
     pygame.draw.rect(screen,optionButton.color2,optionButton.rect,2)
  
  fontObj = font.render('PIANO CATS', True, (255,255,255))
  testRect  = fontObj.get_rect(center= screen.get_rect().center)
  testRect = testRect.move(0,-100)
  screen.blit(fontObj, testRect)

  pygame.display.flip()
  return True

def levelSelect():
  global comic
  global tempY
  screen.fill((0, 0, 0))
  for button in levelButtons:
    pygame.draw.rect(screen, button.color1,button.rect,2)
    comicObj = comic.render(button.text,True,(255,255,255))
    comicRect = comicObj.get_rect(topleft = (button.x,button.y))
    x= 30
    while comicRect.width+10 > button.rect.width:
        x -=1
        comic = pygame.font.Font("Qdbettercomicsans-jEEeG.ttf" , x)
        comicObj = comic.render(button.text,True,(255,255,255))
        comicRect = comicObj.get_rect(topleft = (button.x,button.y))
    comicRect = comicRect.move(button.width/2-(comicRect.width/2),button.height/2-(comicRect.height/2))
    screen.blit(comicObj,comicRect)
    for ev in pygame.event.get(): 
        if ev.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit()
  pygame.display.flip()
  return True
while True:
    levelSelect()
    clock.tick(60)