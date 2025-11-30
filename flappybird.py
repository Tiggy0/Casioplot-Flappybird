from casioplot import *
from random import randint
#import pygame

class Rect():

    def __init__(self,topLeft=(0,0),bottomRight=(10,10),colour=(0,0,0)):
        self.topLeft=topLeft
        self.bottomRight=bottomRight
        self.colour=colour

    def draw(self):
        for x in range(self.topLeft[0],self.bottomRight[0]+1):
            for y in range(self.topLeft[1],self.bottomRight[1]+1):
                set_pixel(x,y,self.colour)
    
    def move(self,amount):
        self.topLeft=((self.topLeft[0])+amount[0],self.topLeft[1]-amount[1])
        self.bottomRight=(self.bottomRight[0]+amount[0],self.bottomRight[1]-amount[1])

class Pipe():
    _registry=[]
    
    def __init__(self,xpos,height):
        self.xpos=xpos
        self.height=191-height
        self.cleared=False
        self.delete=False
        
        self.bottom = Rect((xpos-20,height+30),(xpos+20,191),(117, 191, 48))
        self.top = Rect((xpos-20,0),(xpos+20,height-30),(117, 191, 48))
        
        Pipe._registry.append(self)
    
    def move(self,amount):
        self.bottom.move(amount)
        self.top.move(amount)
    
    def checkCollisions(self):
        if (bird.topLeft[1]<=self.top.bottomRight[1] or bird.bottomRight[1]>=self.bottom.topLeft[1]) and bird.bottomRight[0] >= self.top.topLeft[0] and bird.topLeft[0] <= self.bottom.bottomRight[0]:
            return True
    
    def birdPassed(self):
        if self.top.bottomRight[0]<bird.topLeft[0] and self.cleared==False:
            self.cleared=True
            global score
            score+=1
            Pipe._registry.append(Pipe(360,randint(30,125)))
            self.delete=True
            
    def draw(self):
        self.top.draw()
        self.bottom.draw()

class Bird(Rect):
    def __init__(self,size=(20,20),start=(40,90),colour=(249, 241, 36)):
        self.colour=colour
        
        self.topLeft=(start[0]-int(1/2*size[0]),start[1]-int(1/2*size[1]))
        self.bottomRight=(start[0]+int(1/2*size[0]),start[1]+int(1/2*size[1]))
    
    def isCrashed(self):
        if self.bottomRight[1] >=191:
            return True

def main():
    global bird
    global score
    playing=True
    while playing == True:
        clear_screen()
        
        #moving
        bird.move((0,-5))
        for i in Pipe._registry: i.move((-5,0))
        
        #inputs
        
        key=str(getkey())
        if key in continueKeys: bird.move((0,10))
        elif str(key)=="12": playing = False
        elif str(key)=="36": playing = "Pause"

        #collisions
        for i in Pipe._registry:
            i.birdPassed()
            if i.checkCollisions(): playing = False
        if bird.isCrashed(): playing = False
        
        #draws
        for i in Pipe._registry: i.draw()
        bird.draw()
        draw_string(0,0,("Score: "+str(score)),(0,0,0),"medium")
        
        new_pipes=[]
        for i in Pipe._registry:
            if i.delete==False: new_pipes.append(i)
        Pipe._registry=new_pipes
        
        show_screen()
    if playing == "Pause":
        pause()
    end()

def end():
    draw_string(150,90,("Score: "+str(score)),(0,0,0),"medium")
    show_screen()
    print("Your score was "+str(score)+" pipes passed")

def pause():
    draw_string(150,90,("Paused, Score: "+str(score)),(0,0,0),"medium")
    show_screen()
    while not (str(getkey()) in continueKeys):
        pass
    main()

bird = Bird()
score=0
continueKeys=("24","95")
Pipe._registry.append(Pipe(195,95))
Pipe._registry.append(Pipe(360,randint(30,125)))

main()