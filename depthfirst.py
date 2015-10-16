## Depthfirst spanning tree maze algorithm

import pygame
import sys
from pygame.locals import *
import numpy
import random
import time

sys.setrecursionlimit(20000)

white = 0xffffff
black = 0x000000
running = True
mazeWidth = 51
mazeHeight = 51
multiple = 10
visitedArray = numpy.zeros((mazeWidth, mazeHeight), dtype=bool)
stack = []

pygame.init()
screen = pygame.display.set_mode((mazeWidth*multiple, mazeHeight*multiple))
screen_rect = screen.get_rect()

background = pygame.Surface(screen.get_size()).convert()
background.fill(white)
screen.blit(background, (0,0))
pygame.display.update()

def update_cell(width, height):
    draw_cell((width, height))
    visitedArray[width][height] = True
    neighbors = getNeighbors(width, height)
    if neighbors:
        rand = random.randint(0, len(neighbors)-1)
        randNeighbor = neighbors[rand]
        draw_cell(wall_between(randNeighbor, width, height))
        stack.append(randNeighbor)
        update_cell(randNeighbor[0], randNeighbor[1])
    elif stack:
        new = stack.pop()
        update_cell(new[0], new[1])
    #else:
    #    running = False

def getNeighbors(width, height):
    neighbors = []
    
    if width+2 <= mazeWidth:
        if not visitedArray[width+2][height]:
            neighbors.append((width+2,height))
    if width-2 >= 0:
        if not visitedArray[width-2][height]:
            neighbors.append((width-2,height))
                
    if height+2 <= mazeHeight:
        if not visitedArray[width][height+2]:
            neighbors.append((width,height+2))
    if height-2 >= 0:
        if not visitedArray[width][height-2]:
            neighbors.append((width,height-2))

    return neighbors


def draw_cell(size):
    screen.fill(black, (size[0]*multiple, size[1]*multiple, multiple, multiple))
    pygame.display.update()

def wall_between(neighbor, width, height):
    returnWidth = (width+neighbor[0]) / 2
    returnHeight = (height+neighbor[1]) / 2
    return (returnWidth, returnHeight)

def update_edges():
    for i in range(mazeWidth):
        for j in range(mazeHeight):
            if i == 0 or i == mazeWidth-1 or j == 0 or j == mazeHeight-1:
                draw_cell((i,j))

while running:

    update_edges()
    update_cell(mazeWidth-1, 0)

    for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_RETURN) or event.type == QUIT:
                running = False


pygame.quit()
