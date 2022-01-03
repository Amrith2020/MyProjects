import math
import random
from tkinter.constants import S
import pygame
import tkinter as tk
from tkinter import messagebox
from pygame.display import set_mode

from pygame.version import PygameVersion

class cube(object):
    rows = 20
    w = 500
    def __init__(self,start,dirnx=1, dirny=0, color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self,dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        # gap or distance between x and y
        dis = self.w // self.rows
        # i row and j column
        i = self.pos[0]
        j = self.pos[1]
        #drawing rectangle inside of the square so that grid line is visible, so we dont cover white line, draw inside of the square 
        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        if eyes:
            # circle eyes
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)


class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos) # head of snake
        self.body.append(self.head) 
        # keep track of what direction we are moving
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            #to quit game
            if event.type == pygame.QUIT:
                pygame.quit()
            # dictionary of pressed key values and if they were pressed or not
            keys = pygame.key.get_pressed()
            # for all keys return 1 or 0 depending on whether pressed or not
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    # turns dictionary, self.head.pos[:] is the current position of head of snake, self.dirnx,self.dirny will tell us the turn taken
                    self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
                
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    # turns dictionary, self.head.pos[:] is the current position of head of snake, self.dirnx,self.dirny will tell us the turn taken
                    self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    # turns dictionary, self.head.pos[:] is the current position of head of snake, self.dirnx,self.dirny will tell us the turn taken
                    self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    # turns dictionary, self.head.pos[:] is the current position of head of snake, self.dirnx,self.dirny will tell us the turn taken
                    self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
        
        '''move our cube - a bit complicated, self.body has index i and cube object c, self.body is made of cube objects (line 26)'''
        for i, c in enumerate(self.body):
            # grab position of cube object
            p = c.pos[:]
            # we added position of head to turns, if position is in turns then we move
            # if position p is in turn list, 
            if p in self.turns:
                # actual move, is turn list at that index, 
                turn = self.turns[p]
                # cube.move will get x and y 
                c.move(turn[0],turn[1])
                # if we are in last cube we remove that turn, if we leave it, anytime we hit that list we automatically change directions
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                # checking if we reached edge of screen, if moving left change and it goes to right, counting from zero
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                # if moving right and edge of screen move back to left
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                #if going down, move back up to top
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                #if going up, move back up to down  
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                # if not edge of screen then keep moving
                else: c.move(c.dirnx,c.dirny)
        
    
    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        # checking what direction we're moving, the tail, append a new cube one plus the opposite side of snake move  here---->    <----here like that
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))
 
        # set the direction for cube, tail is moving at the current 
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy



    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                # if first one draw eyes
                c.draw(surface, True)
            else:
                c.draw(surface)

def drawGrid(w, rows, surface):
    '''gap between lines of grid'''
    sizeBtwn = w//rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
        '''for loop to draw lines for the grid'''
        pygame.draw.line(surface, (255,255,255), (x,0), (x,w)) # vertical line
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y)) # horizontal line


def redrawWindow(surface):
    global rows, square_width, s, snack
    '''black screen color 0,0,0'''
    surface.fill((0,0,0))
    '''draw snack'''
    snack.draw(surface)
    '''draw snake'''
    s.draw(surface)
    '''draw grid'''
    drawGrid(square_width, rows, surface)
    pygame.display.update()

def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        # to avoid putting snack on top of snake
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
    return (x,y)

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    global square_width, rows, s, snack
    square_width = 500
    height = 500
    rows = 20
    '''square has same width and height so passing square_width x square_width'''
    win = pygame.display.set_mode((square_width,square_width))
    s = snake((255,0,0), (10,10))
    snack = cube(randomSnack(rows, s), color = (0,123,17))
    flag = True
    '''clock so game doesn't run within 10 frames per second '''
    clock = pygame.time.Clock()
    while flag:
        '''create a delay so that program doesnt run too fast'''
        pygame.time.delay(180)
        '''so snake moves 10 blocks in one second - delay and clock tick is for controlling the speed'''
        clock.tick(20)
        # everytime main runs run s.move
        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color = (0,255,0))
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos, s.body[x+1:])):
                print('Score: ',len(s.body))
                message_box("Good Job Kukudu!","Play Again?")
                s.reset((10,10))
        '''win is the pygame.display.set_mode'''
        redrawWindow(win)
        


main()


