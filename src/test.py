import pygame
import random

TILE_SIZE = 64
NB_TILE_HEIGHT = 10
NB_TILE_WIDTH = 10
WIN_HEIGHT = TILE_SIZE * NB_TILE_HEIGHT
WIN_WIDTH = TILE_SIZE * NB_TILE_WIDTH

pygame.init()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
done = False

class Castle:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.top = pygame.image.load('..\sprites\Structure\medievalStructure_02.png').convert_alpha()
        self.bot = pygame.image.load('..\sprites\Structure\medievalStructure_06.png').convert_alpha()
    
    def draw(self):
        screen.blit(self.top, (self.x*TILE_SIZE,self.y*TILE_SIZE))
        screen.blit(self.bot,(self.x*TILE_SIZE,(self.y+1)*TILE_SIZE))

grass1 = pygame.image.load('..\sprites\Tile\medievalTile_57.png').convert_alpha()
grass2 = pygame.image.load('..\sprites\Tile\medievalTile_58.png').convert_alpha()
tree = pygame.image.load('..\sprites\Tile\medievalTile_42.png').convert_alpha()


def grass_fill():
    for i in range(0,WIN_WIDTH,64):
        for j in range(0,WIN_HEIGHT,64):
            rand = random.randint(1,8)
            if rand in [1,4]:
                screen.blit(grass1,(i,j))
            elif rand == 5:
                screen.blit(tree,(i,j))
            else:
                screen.blit(grass2,(i,j))

def move_up(x,y):
    return x,y-TILE_SIZE

def move_down(x,y):
    return x,y+TILE_SIZE

def move_left(x,y):
    return x-TILE_SIZE,y

def move_right(x,y):
    return x+TILE_SIZE,y

def draw_path(start_x,start_y,end_x,end_y):
    start_x *= 64
    start_y *= 64
    end_x *= 64
    end_y *= 64

    pos_x = move_down(start_x,start_y)[0]
    pos_y = move_down(start_x,start_y)[1]

    visited = []







grass_fill()
c1 = Castle(7,5)
c1.draw()
c2 = Castle()
c2.draw


c2 = Castle(4,3)
c2.draw()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        pygame.display.flip()
