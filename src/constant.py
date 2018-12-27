TILE_SIZE = 64
TILE = [TILE_SIZE,TILE_SIZE]
NB_TILE_WIDTH =19 #ww2|16 - barrack|20 - joust|19 - necklace|21
NB_TILE_HEIGHT =7 #ww2|9 - barrack|11 - joust|7 - necklace|9
WIN_SIZE = [NB_TILE_WIDTH*TILE_SIZE,NB_TILE_HEIGHT*TILE_SIZE]
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def updateSize(plt):
    NB_TILE_WIDTH = len(plt.interface[0])
    NB_TILE_HEIGHT = len(plt.interface)
    WIN_SIZE = [NB_TILE_WIDTH*TILE_SIZE,NB_TILE_HEIGHT*TILE_SIZE]
    return WIN_SIZE

