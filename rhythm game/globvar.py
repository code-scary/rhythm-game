from re import X
import pygame, sys
from pygame import mixer 
from pygame.locals import *
from pygame.math import Vector2
from pygame.image import load
from pygame.transform import rotozoom
from math import sqrt
import random
pygame.init()
mixer.init()
clock = pygame.time.Clock()
width = 700
height = 700
#Center Rect info
cWidth = 150
cHeight = 150
cColor = (0,0,0)
subCWidth = 50
subCColor = (100,100,100)
# light shade of the button
color_light = (170,170,170)
# dark shade of the button
color_dark = (100,100,100)
speed = 5
screen = pygame.display.set_mode((width,height))
cX = screen.get_rect().centerx- cWidth/2
cY = screen.get_rect().centery-cHeight/2
cSquare = pygame.Rect(cX, cY, cWidth,cHeight)
aHeld = False
wHeld = False
dHeld = False
sHeld = False
spaceHeld = False

