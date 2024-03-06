import pygame 

pygame.init()

screen = pygame.display.set_mode([500,500])

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)

screen.fill(WHITE)

class My_circle():
    def __init__(self, color, pos, radius, width = 0):
        self.color = color 
        self.radius = radius 
        self.pos = pos 
        self.width = width 
        self.screen = screen
        
    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius, self.width)
        
    def grow(self, x):
        self.radius += x
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius, self.width)






#creating circle without circle of the calss 
position = (300,300)
radius = 50 
width = 2
pygame.draw.circle(screen, YELLOW, position, radius, width)

pygame.display.update()

#creating objects
blue_circle = My_circle(BLUE, position, radius + 60)
red_circle = My_circle(RED, position, radius + 40)
green_circle = My_circle(GREEN, position, radius, 5)
yellow_circle = My_circle(YELLOW, position, 20)




