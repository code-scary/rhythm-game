from globvar import *
def load_sprite(name, transparent):
    path = f"assets/sprites/"+name+".png"
    sprite = load(path)

    if transparent == True:
        return sprite.convert_alpha()
    else:
        return sprite.convert()
class gameObject():
    def __init__(self, position, sprite, velocity):
        self.x = position[0]
        self.y = position[1]
        self.velocity = velocity
        self.radius = sprite.get_height()/2
        self.velocity = velocity
        self.vectocity = Vector2(velocity)
        self.sprite = sprite
        self.position = position
        self.vecposition = Vector2((self.x,self.y))
        self.cheeserect = sprite.get_rect()
    def draw(self,surface):
        blit_position = ((self.x-self.sprite.get_width()/2, self.y-self.sprite.get_width()/2))
        surface.blit(self.sprite, blit_position)
        pygame.draw.rect(self.sprite, (250,0,0), self.cheeserect, 1)
    def move(self, surface):
        self.vecposition = self.vecposition + self.vectocity
       # print(self.vecposition)
        self.x = self.vecposition[0]
        self.y = self.vecposition[1]
    def collision(self, otherObj): 
        rise = (self.y-self.radius)-(otherObj.y-otherObj.radius)
        run = (self.x-self.radius)-(otherObj.x-otherObj.radius)
        hypotenuse = sqrt(rise**2+run**2)
        pygame.draw.line(screen, (255,255,255), (self.x-self.radius,self.y-self.radius), (otherObj.x-otherObj.radius,otherObj.y-otherObj.radius))
        distance_line = self.radius+otherObj.radius-15

        if  hypotenuse > distance_line:
            return False
        if hypotenuse < distance_line:
            return True
        else:
            return False


class asteroids(gameObject):
    def __init__(self, position, time, directionality):
        super().__init__(position, pygame.transform.scale(load_sprite("asteroid",True), (40, 40)), speed)
        self.position = position
        self.time = time*100
        self.directionality = directionality 
        self.speed = speed
        #self.asteroid = figure this one out now, need to do the thing the tutorials sorta do 
    def move(self):
        if self.directionality == 0 and self.time <= 0:
            self.x += self.velocity
            self.track = abs(self.x)
            return self.track
        elif self.directionality == 1 and self.time<=0:
            self.y += self.velocity
            self.track = abs(self.y)
            return self.track
        elif self.directionality == 2 and self.time<=0:
            self.x -= self.velocity
            self.track = abs(self.x)
            return self.track
        elif self.directionality == 3 and self.time <= 0:
            self.y -= self.velocity
            self.track = abs(self.y)
            return self.track
        else:
            self.time-=1
            return 0
DOWN = Vector2(0,-1)
class player_object(gameObject):
    accel = .25
    
    def __init__(self, position, callBack):
        
        super().__init__(position, pygame.transform.scale(load_sprite("space_cat_sprite1",True), (40,40)),0 )
        self.coord = (2,2)
        self.spinSpeed = 10
        self.direction = Vector2(DOWN)
        self.position = (self.x, self.y)
        self.callBack = callBack
        self.bullSpeed=3
        self.spinD = 0
        sprite2 = pygame.transform.scale(load_sprite("space_cat_sprite2",True), (50,50))
    def accelerate(self):
        self.vectocity = self.direction/self.accel
    def altMove(self, direc):
        if direc == 1 and self.coord[0]>1:
            self.x -= 50
            coordx =self.coord[0]-1
            coordy=self.coord[1]
            self.coord = (coordx,coordy)
        if direc == 2 and self.coord[1]>1:
            self.y -= 50
            coordx =self.coord[0]
            coordy=self.coord[1]-1
            self.coord = (coordx,coordy)
        if direc == 3 and self.coord[0]<3:
            self.x += 50
            coordx = self.coord[0]+1
            coordy=self.coord[1]
            self.coord = (coordx,coordy)
        if direc == 4 and self.coord[1]<3:
            self.y+=50
            coordx = self.coord[0]
            coordy=self.coord[1]+1
            self.coord = (coordx,coordy)
    def speen(self, direc):
        if direc == 0:
            self.spinD = (0,-1)
        elif direc == 1: 
            self.spinD= (-1,0)
        elif direc == 2:
            self.spinD = (0,1)
        elif direc == 3:
            self.spinD =(1,0)
        print(direc)
        
        #self.direction.rotate_ip(angle)
    def draw(self, surface):
        spinVector = Vector2(self.spinD)
        
        print(str(spinVector)+" Spin")
        print(str(DOWN)+" DOWN")
        angle = spinVector.angle_to(DOWN)
        print(str(angle)+" Angle")
        rotated_image = rotozoom(self.sprite, angle,1.0)
        rotation_size = rotated_image.get_size()
        blit_position = ((self.x-rotated_image.get_width()/2, self.y-rotated_image.get_width()/2))
        surface.blit(rotated_image, blit_position)
        self.cheeserect = self.sprite.get_rect()
        pygame.draw.rect(self.sprite, (250,0,0), self.cheeserect, 1)
    def shoot(self):
        
        
        bullet = Bullet(self.position,self.bullSpeed)
        self.callBack(bullet)
bulletColor = (0,0,0)
channel = 0
math = 1
class Bullet(gameObject):
    def __init__(self, position, velocity):
        super().__init__(position, pygame.transform.scale(load_sprite("note_bullet",True), (30,25)), velocity)
        self.position = position
        self.velocity = velocity
        self.color = bulletColor
        self.channel = channel
        self.math = math
        self.prevColor = (0,0,0)

    
    def colorChangeHelper(self, color, channel, math):
        color = list(color)
        colorSpeed = 70
        if math == 0:
            if color[channel]-colorSpeed > 0: #if the new value is within the max keep going
                tempColor = list(color)
                tempColor[channel] -= colorSpeed
                color = tempColor
                return color, channel, True

            elif color[channel]-colorSpeed <= 0: # if it goes over branch
                color[channel] =  0 
                if channel < 2:  #creating a variable to keep track of the prior channel 
                    nextchannel = channel+1
                else:
                    nextchannel = 0
 
                return color, nextchannel, False
        
        elif math == 1:
            if color[channel]+colorSpeed <= 250: #if the new value is within the max keep going
                tempColor = list(color)
                tempColor[channel] += colorSpeed
                color = tempColor
                return color, channel, True

            elif color[channel]+colorSpeed > 250: # if it goes over branch
                color[channel] =  250 
                if channel > 0:  #creating a variable to keep track of the prior channel 
                    backchannel = channel-1
                else:
                    backchannel = 2

                if color[backchannel]==0: # if we max out the current channel and the last one is at 0 we should start adding to the next channel
                    if channel == 2: #if were on the last channel next should be the first   
                        channel = 0
                        return color, channel, True
                    else:
                        return color, channel+1, True
                else:
                    return color, backchannel, False #should begin subracting from previous channel otherwise
    
    def colorChange(self):
        self.prevColor = self.color
        colorInfo = self.colorChangeHelper(self.color, self.channel, self.math)
        self.color = tuple(colorInfo[0])
        self.channel = colorInfo[1]
        if not colorInfo[2]:
            if self.math ==0:
                self.math = 1
            else:
                self.math = 0
        pixels = pygame.PixelArray(self.sprite)
        pixels.replace(self.prevColor, self.color)
        del pixels
        self.draw(screen)