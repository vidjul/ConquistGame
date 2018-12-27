import pygame
import random
from pygame.locals import *
import sprite as spt

import constant as cst
import models

pygame.init()

menu = pygame.display.set_mode((1700, 700))
menu.blit(spt.joust, (0, 0))
menu.blit(spt.barrack, (850, 0))
menu.blit(spt.necklace, (0, 350))
menu.blit(spt.ww2, (850, 350))
pygame.display.flip()

choose_map = False
pygame.display.set_caption('Choose a map')

while (not choose_map):
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            mx, my = pygame.mouse.get_pos()
            if mx < 850:
                if my < 350:
                    plt_name = 'joust'
                else:
                    plt_name = 'necklace'
            else:
                if my < 350:
                    plt_name = 'barrack'
                else:
                    plt_name = 'WWII'
            choose_map = True

#pltName = random.choice(models.gamePlatforms.games.keys())
plt = models.gamePlatforms.games[plt_name]
# plt.setToOneVOne()

screen = pygame.display.set_mode(cst.updateSize(plt))
pygame.display.set_caption(plt_name)


def win_init(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            path = spt.Path(i, j)
            path.draw(screen, 'grs')


def draw_path(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if '_' not in matrix[i][j]:
                path = spt.Path(i, j)
                path.draw(screen, matrix[i][j].lower())


def draw_struct(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if '_' in matrix[i][j]:
                value = matrix[i][j].split('|')
                sprite = spt.sprite_from_id(value, i, j, plt)
                sprite.draw(screen)


def win_updt(matrix):
    win_init(matrix)
    draw_path(matrix)
    draw_struct(matrix)


def get_click_elem(matrix, plt, mx, my):
    col = my / cst.TILE_SIZE
    line = mx / cst.TILE_SIZE
    value = matrix[col][line].split('|')
    if len(value) == 2:
        return (plt.getVertex(int(value[1])), line, col)
    else:
        return (None, line, col)


def pick_two_elem(color):
    elem_list = []
    temps = []
    while len(elem_list) != 2:
        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONDOWN):
                temp = get_click_elem(plt.interface, plt,
                                      *pygame.mouse.get_pos())
                temps.append(temp)
                if len(elem_list) == 0:
                    if temp[0] is not None:
                        if temp[0].color == color:
                            elem_list.append(temp[0])
                            screen.blit(
                                spt.border, (temp[1] * 64, temp[2] * 64))
                            pygame.display.flip()
                            unit_nbr = input_unit_nbr(screen, '')
                        else:
                            print 'not a valid color'
                            error_pop_up(screen, 0)

                else:
                    if temp[0] is not None:
                        if temp[0].isNeighbor(elem_list[0]) or temp[0] == elem_list[0]:
                            elem_list.append(temp[0])
                        else:
                            print 'not a valid struct'
                            error_pop_up(screen, 1)
                            screen.blit(
                                spt.border, (temps[0][1] * 64, temps[0][2] * 64))
                            pygame.display.flip()
    return (elem_list, unit_nbr)


def input_unit_nbr(screen, unit_nbr):
    valid_input = False
    change = False
    while (not valid_input):
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_BACKSPACE):
                    unit_nbr = unit_nbr[:-1]
                    change = True
                if (event.key == K_0):
                    unit_nbr += '0'
                    change = True
                if (event.key == K_1):
                    unit_nbr += '1'
                    change = True
                if (event.key == K_2):
                    unit_nbr += '2'
                    change = True
                if (event.key == K_3):
                    unit_nbr += '3'
                    change = True
                if (event.key == K_4):
                    unit_nbr += '4'
                    change = True
                if (event.key == K_5):
                    unit_nbr += '5'
                    change = True
                if (event.key == K_6):
                    unit_nbr += '6'
                    change = True
                if (event.key == K_7):
                    unit_nbr += '7'
                    change = True
                if (event.key == K_8):
                    unit_nbr += '8'
                    change = True
                if (event.key == K_9):
                    unit_nbr += '9'
                    change = True
                if (event.key == K_PLUS):
                    unit_nbr = str(int(unit_nbr) + 1)
                    change = True
                if (event.key == K_PLUS):
                    unit_nbr = str(int(unit_nbr) + -1)
                    change = True
                if (event.key == K_RETURN):
                    valid_input = True
        font = pygame.font.Font(None, 25)
        disp_unit_nbr = font.render('x ' + unit_nbr, False, cst.BLACK)
        if (change):
            screen.blit(spt.grs, (0, 0))
            screen.blit(disp_unit_nbr, (0, 0))
            pygame.display.flip()
    return int(unit_nbr)


def error_pop_up(screen, error_index):
    error = spt.error()
    error.draw(screen, error_index)
    pygame.display.flip()
    not_clicked_on_error = True
    while (not_clicked_on_error):
        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONDOWN):
                mx, my = pygame.mouse.get_pos()
                if (mx > error.rects[error_index][0] and mx < error.rects[error_index][0] + 320):
                    if (my > error.rects[error_index][1] and my < error.rects[error_index][1] + 128):
                        win_updt(plt.interface)
                        pygame.display.flip()
                        not_clicked_on_error = False


win_init(plt.interface)


turn = 1
player = plt.firstPlayerBaseKey

win_updt(plt.interface)
pygame.display.flip()

while not plt.gameOver():
    # win_updt(plt.interface)
    # pygame.display.flip()
    if plt.getVertex(player).color == 0:
        plt.movingIa()
        player = plt.secondPlayerBaseKey
        plt.nextTurn()
        win_updt(plt.interface)
        pygame.display.flip()

    else:
        sameColor = True
        while(sameColor):
            picked_elem, unit_nbr = pick_two_elem(plt.getVertex(player).color)
            if(picked_elem[0].color != picked_elem[1].color):
                sameColor = False
            picked_elem[0].moveSoldiers(
                picked_elem[1], unit_nbr)
            win_updt(plt.interface)
            pygame.display.flip()
            if (not sameColor or picked_elem[0] == picked_elem[1]):
                if player == plt.firstPlayerBaseKey:
                    player = plt.secondPlayerBaseKey
                else:
                    player = plt.firstPlayerBaseKey
                plt.nextTurn()
                win_updt(plt.interface)
                pygame.display.flip()
                break

    turn += 1
game_over = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Game Over !')
if plt.getVertex(plt.firstPlayerBaseKey).color in (0, 2):
    game_over.blit(spt.red_wins, (0, 0))
else:
    game_over.blit(spt.blue_wins, (0, 0))
pygame.display.flip()
close_game = False
while(not close_game):
    for event in pygame.event.get():
        if (event.type == QUIT):
            close_game = True
