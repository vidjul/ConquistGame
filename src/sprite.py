import pygame

import constant as cst


pixel = pygame.display.set_mode((0, 0))

unit = pygame.image.load('..\sprites\unit\unit.png')

base_img = pygame.image.load(
    '..\sprites\structure\\base.png').convert_alpha()
house_img = pygame.image.load(
    '..\sprites\structure\house.png').convert_alpha()
tower_top = pygame.image.load(
    '..\sprites\structure\\tow_top.png').convert_alpha()
tower_bot = pygame.image.load(
    '..\sprites\structure\\tow_bot.png').convert_alpha()
castle_top = pygame.image.load(
    '..\sprites\structure\\cst_top.png').convert_alpha()
castle_bot = pygame.image.load(
    '..\sprites\structure\\cst_bot.png').convert_alpha()

grs = pygame.image.load(
    '..\sprites\path\grs.png').convert_alpha()
ver = pygame.image.load(
    '..\sprites\path\\ver.png').convert_alpha()
hor = pygame.image.load(
    '..\sprites\path\hor.png').convert_alpha()
upl = pygame.image.load(
    '..\sprites\path\upl.png').convert_alpha()
upr = pygame.image.load(
    '..\sprites\path\upr.png').convert_alpha()
dwl = pygame.image.load(
    '..\sprites\path\dwl.png').convert_alpha()
dwr = pygame.image.load(
    '..\sprites\path\dwr.png').convert_alpha()
edw = pygame.image.load(
    '..\sprites\path\edw.png').convert_alpha()
eup = pygame.image.load(
    '..\sprites\path\eup.png').convert_alpha()
elf = pygame.image.load(
    '..\sprites\path\elf.png').convert_alpha()
erg = pygame.image.load(
    '..\sprites\path\erg.png').convert_alpha()
dwt = pygame.image.load(
    '..\sprites\path\dwt.png').convert_alpha()
upt = pygame.image.load(
    '..\sprites\path\upt.png').convert_alpha()
lft = pygame.image.load(
    '..\sprites\path\lft.png').convert_alpha()
rgt = pygame.image.load(
    '..\sprites\path\\rgt.png').convert_alpha()
crs = pygame.image.load(
    '..\sprites\path\crs.png').convert_alpha()
blue_wins = pygame.image.load('..\sprites\gui\\blue_wins.png').convert_alpha()
red_wins = pygame.image.load('..\sprites\gui\\red_wins.png').convert_alpha()

error_struct = pygame.image.load('..\sprites\gui\error_struct.png')
error_neighbor = pygame.image.load('..\sprites\gui\error_neighbour.png')

border = pygame.image.load('..\sprites\gui\\border.png')

joust = pygame.image.load('..\sprites\gui\joust.png')
barrack = pygame.image.load('..\sprites\gui\\barrack.png')
necklace = pygame.image.load('..\sprites\gui\\necklace.png')
ww2 = pygame.image.load('..\sprites\gui\\ww2.png')


class Nexus:
    def __init__(self, col, line, key, graph):
        self.key = key
        self.col = col
        self.line = line
        self.img = base_img
        self.unit = unit
        self.unit_nb = graph.getVertex(key).soldiers
        self.color = graph.getVertex(key).color
        self.rect = [line * cst.TILE_SIZE, col * cst.TILE_SIZE]
        self.u_rect = [[line * cst.TILE_SIZE - 16, col * cst.TILE_SIZE - 48],
                       [line * cst.TILE_SIZE + 32, col * cst.TILE_SIZE - 24]]

    def draw(self, screen):
        screen.blit(self.img, self.rect)
        screen.blit(self.unit, self.u_rect[0])
        font = pygame.font.Font(None, 25)
        if self.color == 1:
            text_color = cst.BLUE
        elif self.color in (0, 2):
            text_color = cst.RED
        elif self.color == -1:
            text_color = cst.BLACK
        text = font.render('x ' + str(self.unit_nb), False, text_color)
        screen.blit(text, self.u_rect[1])


class House:
    def __init__(self, col, line, key, graph):
        self.key = key
        self.col = col
        self.line = line
        self.img = house_img
        self.unit = unit
        self.unit_nb = graph.getVertex(key).soldiers
        self.color = graph.getVertex(key).color
        self.rect = [line * cst.TILE_SIZE, col * cst.TILE_SIZE]
        self.u_rect = [[line * cst.TILE_SIZE - 16, col * cst.TILE_SIZE - 48],
                       [line * cst.TILE_SIZE + 32, col * cst.TILE_SIZE - 24]]

    def draw(self, screen):
        screen.blit(self.img, self.rect)
        screen.blit(self.unit, self.u_rect[0])
        font = pygame.font.Font(None, 25)
        if self.color == 1:
            text_color = cst.BLUE
        elif self.color in (0, 2):
            text_color = cst.RED
        elif self.color == -1:
            text_color = cst.BLACK
        text = font.render('x ' + str(self.unit_nb), False, text_color)
        screen.blit(text, self.u_rect[1])


class Tower:
    def __init__(self, col, line, key, graph):
        self.key = key
        self.col = col
        self.line = line
        self.img_top = tower_top
        self.img_bot = tower_bot
        self.unit = unit
        self.unit_nb = graph.getVertex(key).soldiers
        self.color = graph.getVertex(key).color
        self.top = [line * cst.TILE_SIZE, (col - 1) * cst.TILE_SIZE + 21]
        self.bot = [line * cst.TILE_SIZE, col * cst.TILE_SIZE + 21]
        self.u_rect = [[line * cst.TILE_SIZE - 16, col * cst.TILE_SIZE - 64],
                       [line * cst.TILE_SIZE + 32, col * cst.TILE_SIZE - 38]]

    def draw(self, screen):
        screen.blit(self.img_top, self.top)
        screen.blit(self.img_bot, self.bot)
        screen.blit(self.unit, self.u_rect[0])
        font = pygame.font.Font(None, 25)
        if self.color == 1:
            text_color = cst.BLUE
        elif self.color in (0, 2):
            text_color = cst.RED
        elif self.color == -1:
            text_color = cst.BLACK
        text = font.render('x ' + str(self.unit_nb), False, text_color)
        screen.blit(text, self.u_rect[1])


class Castle:
    def __init__(self, col, line, key, graph):
        self.key = key
        self.col = col
        self.line = line
        self.img_top = castle_top
        self.img_bot = castle_bot
        self.unit = unit
        self.unit_nb = graph.getVertex(key).soldiers
        self.color = graph.getVertex(key).color
        self.top = [line * cst.TILE_SIZE, (col - 1) * cst.TILE_SIZE + 21]
        self.bot = [line * cst.TILE_SIZE, col * cst.TILE_SIZE + 21]
        self.u_rect = [[line * cst.TILE_SIZE - 16, col * cst.TILE_SIZE - 64],
                       [line * cst.TILE_SIZE + 32, col * cst.TILE_SIZE - 38]]

    def draw(self, screen):
        screen.blit(self.img_top, self.top)
        screen.blit(self.img_bot, self.bot)
        screen.blit(self.unit, self.u_rect[0])
        font = pygame.font.Font(None, 25)
        if self.color == 1:
            text_color = cst.BLUE
        elif self.color in (0, 2):
            text_color = cst.RED
        elif self.color == -1:
            text_color = cst.BLACK
        text = font.render('x ' + str(self.unit_nb), False, text_color)
        screen.blit(text, self.u_rect[1])


def sprite_from_id(id, col, line, graph):
    if id[0] == '_HSE':
        return House(col, line, int(id[1]), graph)
    elif id[0] == '_TOW':
        return Tower(col, line, int(id[1]), graph)
    elif id[0] == '_CST':
        return Castle(col, line, int(id[1]), graph)
    elif id[0] == '_NXS':
        return Nexus(col, line, int(id[1]), graph)
    else:
        return None


class Path:
    def __init__(self, col, line):
        self.col = col
        self.line = line
        self.grs = grs
        self.ver = ver
        self.hor = hor
        self.upl = upl
        self.upr = upr
        self.dwl = dwl
        self.dwr = dwr
        self.edw = edw
        self.eup = eup
        self.elf = elf
        self.erg = erg
        self.dwt = dwt
        self.upt = upt
        self.lft = lft
        self.rgt = rgt
        self.crs = crs

        self.rect = [self.line * cst.TILE_SIZE, self.col * cst.TILE_SIZE]

    def draw(self, screen, elem):
        screen.blit(getattr(self, elem), self.rect)


def hud(msg, screen):
    font = pygame.font.Font(None, 25)
    text = font.render(msg, False, cst.BLACK)
    screen.blit(text, (0, 0))


class error:
    def __init__(self):
        self.boxes = [error_struct, error_neighbor]
        self.rects = [[(cst.NB_TILE_WIDTH * 32) - 320,
                       (cst.NB_TILE_HEIGHT * 32) - 134],
                      [(cst.NB_TILE_WIDTH - 4) * cst.TILE_SIZE /
                       2, (cst.NB_TILE_HEIGHT + 2) * cst.TILE_SIZE / 2]]

    def draw(self, screen, error_index):
        screen.blit(self.boxes[error_index], self.rects[error_index])
