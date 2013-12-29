import pygame
import sys
from pygame.locals import *

class Paddle:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.speed = 5
        pygame.draw.rect(screen, white, [self.x, self.y, 10, 100])
        
    def moveUp(self):
        self.y = self.y - self.speed
        
    def moveDown(self):
        self.y = self.y + self.speed
        
    def update(self):
        pygame.draw.rect(screen, white, [self.x, self.y, 10, 100])
        
        

class Rect:
    x = 0
    y = 0
    sdx = 5
    sdy = 5
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sdx = 5
        self.sdy = 5
        pygame.draw.rect(screen, white, [self.x, self.y, 50, 50])
        pygame.draw.rect(screen, red, [self.x + 10, self.y + 10, 30, 30])
        
    def bounce(self):
        if self.y > 450 or self.y < 0:
            self.sdy = self.sdy * -1
        if self.x > 650 or self.x < 0:
            self.sdx = self.sdx * -1         
           
    def increaseSpeed(self):
        if self.sdx < 0:
            self.sdx = self.sdx - 1
        else:
            self.sdx = self.sdx + 1
        if self.sdy < 0:
            self.sdy = self.sdy - 1
        else:
            self.sdy = self.sdy + 1 

    def update(self):
        self.x += self.sdx
        self.y += self.sdy
        self.bounce()
        
        pygame.draw.rect(screen, white, [self.x, self.y, 50, 50])
        pygame.draw.rect(screen, green, [self.x + 10, self.y + 10, 30, 30])
        
# Define some colors
black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)

pygame.init()

# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing Rectangle")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

list = []
square = Rect(85, 85)
list.append(square)


plist = []
leftPad = Paddle(10, 20)
plist.append(leftPad)
rightPad = Paddle(680, 20)
plist.append(rightPad)

# Speed and direction of rectangle
rect_change_x = 5
rect_change_y = 5

rect_change_x2 = 5
rect_change_y2 = 5

# -------- Main Program Loop -----------
while done == False:
  for event in pygame.event.get(): # User did something
    if event.type == pygame.QUIT: # If user clicked close
      done = True # Flag that we are done so we exit this loop
      
  # Set the screen background
  screen.fill(black)
  
  for i in range(len(list) -1):
      for j in range(i+1,len(list)):
        dx = list[i].x - list[j].x
        dy = list[i].y - list[j].y
        if abs(dx) < 50 and abs(dy) < 50:
            if abs(dx) < abs(dy):
                list[i].sdy = list[i].sdy * -1 
                list[j].sdy = list[j].sdy * -1
                print(list[i].sdx, list[i].sdy) 
            else:
                #print(list[i].x, list[i].y)
                list[i].sdx = list[i].sdx * -1
                list[j].sdx = list[j].sdx * -1
                
  px = square.x - leftPad.x
  py = square.y - leftPad.y
  if abs(px) < 15 and abs(py) < 50:
     square.sdx = square.sdx * -1
     
  rx = square.x - rightPad.x
  ry = square.x - rightPad.x
  if abs(rx) < 65 and abs(ry) < 50:
      square.sdx = square.sdx * -1  
                  
  if event.type == KEYDOWN:
      if event.key == K_w:
        leftPad.moveUp()
      if event.key == K_s:
        leftPad.moveDown()
          
      if event.key == K_UP:
        rightPad.moveUp()
      if event.key == K_DOWN:
        rightPad.moveDown()
                                   
  
  for rect in list:
      rect.update()
  for pad in plist:
      pad.update()
  
  # Limit to 20 frames per second
  clock.tick(20)
  
  # Go ahead and update the screen with what we've drawn.
  pygame.display.flip()
  
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()