"""
Created on Sat Oct 10 18:19:48 2020

@author: Mohammed Rahman
"""

import pygame #imports pygame module
import pygame_menu #imports start menu module
import sys #imports fonts module
import random #imports random number module

pygame.init() #starts pygame
surface = pygame.display.set_mode((1280, 720)) #sets the window height and length

s_width = 500 #defining window width
s_height = 500 #defining window length

g_size = 10 #defining every cube size in the grid
g_width = s_width/g_size #equation to create the grid's width
g_height = s_height/g_size #equation to create the grid's height

up = (0,-1) #variable for character moving up
down = (0,1) #variable for character moving down
left = (-1,0) #variable for character moving left
right = (1,0) #variable for character moving right

def start_the_game(): #function for start menu
    

    menu = pygame_menu.Menu(height=500,
                            width=800, 
                            theme=pygame_menu.themes.THEME_BLUE,
                            title='Welcome to Feed The Worm: Extreme') #variable for start menu, defines width , length, theme from pygame module and the title

    menu.add_button('Play', main) #adds a pygame menu button called Play
    menu.add_button('Quit', pygame_menu.events.EXIT) #adds a pygame menu button called Quit

    if __name__ == '__main__': #if statement to create the surface for the game on a loop
        menu.mainloop(surface)

def main(): #function for the main part of the game 
    clock = pygame.time.Clock() #variable for using the clock function in pygame
    screen = pygame.display.set_mode((s_width, s_height), 0, 32) #sets the window

    surface = pygame.Surface(screen.get_size()) #sets the surface based on window size
    surface = surface.convert() #converts this into working surface
    drawGrid(surface) #drawgrid variable is set to surface

    worm = Worm() #worm variable is set to Worm function
    food = Food() #food variable is set to Food function

    myfont = pygame.font.SysFont("helvetica_bold",32) #sets the font and size for the scoreboard

    while (True): #while statement for character
        clock.tick(10) #sets clock
        worm.controls() #uses controls function inside worm class
        drawGrid(surface) #drawgrid variable is set to surface
        worm.movement() #uses movement function inside worm class
        if worm.headpos() == food.position: #if statement for the positioning of both the worm and the food
            worm.length += 1
            worm.score += 1
            food.randomize_position() #executes the random position procedure for food
        worm.draw(surface) #draws surface for the worm
        food.draw(surface) #draws surface for the food
        screen.blit(surface, (0,0)) #blit is set to 0,0
        text = myfont.render("Score {0}".format(worm.score), 1, (0,0,0)) #displays score
        screen.blit(text, (5,10)) #blit text is set to 5, 10
        pygame.display.update() #pygame display is updated

class Worm(): #class for the worm character
    def __init__(self): #initiates the worm
        self.length = 1 #sets the worm's length to 1 at the start
        self.positions = [((s_width/2), (s_height/2))] #sets the position for the worm at the start
        self.direction = random.choice([up, down, left, right]) #sets the facing direction for the worm at the start
        self.color = (153, 76, 48) #color is set to RGB code 153, 76, 48

        self.score = 0 #score is set to 0 by default

    def controls(self): #function for the worm controls
        for event in pygame.event.get(): #for loop for controls
            if event.type == pygame.QUIT: #if statement for the controls 
                pygame.quit() #game quits if the event is set to quit
                sys.exit() #sys also exits
            elif event.type == pygame.KEYDOWN: #if statements that create actions based off of certain keypresses
                if event.key == pygame.K_UP or event.key == ord('w'): #if UP key or W key is pressed then worm goes up
                    self.turn(up)
                if event.key == pygame.K_DOWN or event.key == ord('s'): #if DOWN key or S key is pressed then worm goes down
                    self.turn(down)
                if event.key == pygame.K_LEFT or event.key == ord('a'): #if LEFT key or A key is pressed then worm goes left
                    self.turn(left)
                if event.key == pygame.K_RIGHT or event.key == ord('d'): #if RIGHT key or D key is pressed then worm goes right
                    self.turn(right) 

    def headpos(self): #function for the worm's head position
        return self.positions[0] #returns position

    def turn(self, point): #function for worm turning
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction: #if statement for the turning mechanism
            return
        else:
            self.direction = point

    def movement(self): #function for the movement of the worm
        current = self.headpos() #head position is set to current
        x,y = self.direction #X and Y variables are set to self.direction
        new = (((current[0]+(x*g_size))%s_width), (current[1]+(y*g_size))%s_height) #sizes get aligned to new variable
        if len(self.positions) > 2 and new in self.positions[2:]: #if statement for position lens
            self.resetScreen()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def resetScreen(self): #function for restarting the game if u fail
        self.length = 1 #length set to 1
        self.positions = [((s_width/2), (s_height/2))] #position is set
        self.direction = random.choice([up, down, left, right]) #direction is set
        self.score = 0 #score is set back to 0

    def draw(self,surface): #function for drawing the worm surface
        for p in self.positions: #for loop for drawing the surface including colours and shapes
            r = pygame.Rect((p[0], p[1]), (g_size,g_size))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)



class Food(): #class for food
    def __init__(self): #initiates the food class
        self.position = (0,0) #position before it is set
        self.color = (223, 163, 49) #sets the food colour to RGB code 223, 163 , 49
        self.randomize_position() #randomises the position for the code

    def randomize_position(self): #function for randomising positions
        self.position = (random.randint(0, g_width-1)*g_size, random.randint(0, g_height-1)*g_size) #variable for positioning using random numbers

    def draw(self, surface): #function for drawing the food surface
        r = pygame.Rect((self.position[0], self.position[1]), (g_size, g_size)) #variable for the positioning
        pygame.draw.rect(surface, self.color, r) #draws the shape
        pygame.draw.rect(surface, (93, 216, 228), r, 1) #draws the colour

def drawGrid(surface): #function for drawing the surface
    for y in range(0, int(g_height)): #for loop for y axis
        for x in range(0, int(g_width)): #for loop for x axis
            if (x+y)%2 == 0: #if statement for the shape and colours
                r = pygame.Rect((x*g_size, y*g_size), (g_size,g_size))
                pygame.draw.rect(surface,(149,122,68), r)
            else:
                rr = pygame.Rect((x*g_size, y*g_size), (g_size,g_size))
                pygame.draw.rect(surface, (129,109,68), rr)



start_the_game() #starts the whole application with the start menu
