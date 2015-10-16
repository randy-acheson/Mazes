import pygame
from pygame.locals import *
import numpy
import ctypes
import random

running = True
go = True
mazeSize = (30, 20)
pixArray = numpy.zeros((mazeSize), dtype=bool)
wallList = []

pygame.init()
screen = pygame.display.set_mode((mazeSize[0]*10, mazeSize[1]*10))
screen_rect = screen.get_rect()
stack = []

background = pygame.Surface(screen.get_size()).convert()
background.fill(0xffffff)
screen.blit(background, (0, 0))
pygame.display.update()

def update_cell(width, height):
    pixArray[width][height] = True
    neighbors = getUnvisitedNeighbors(width, height)
    if neighbors:
        element = random.randint(0, len(neighbors)-1)
        stack.push(element)
        update_cell(element)
        ##remove_wall
        pixArray[element[0]][element[1]] = True
    elif stack:
        element = stack.pop()
        update_cell(element)
    else:
        randWidth = random.randint(0, mazeSize[0])
        randHeight = random.randint(0, mazeSize[1])
        if pixArray[randWidth][randHeight]:
            update_cell(pixArray[randWidth][randHeight])
            
    ##wallList.extend
    square = pygame.Surface((10, 10))
    square.fill(0x000000)
    screen.blit(square, (width*10, height*10))
    pygame.display.update()

def getUnvisitedNeighbors(width, height):
    neighbors = []
    if pixArray[width-1][height] == False: neighbors.append(pixArray[width-1][height])
    if pixArray[width+1][height] == False: neighbors.append(pixArray[width+1][height])
    if pixArray[width][height-1] == False: neighbors.append(pixArray[width][height-1])
    if pixArray[width][height+1] == False: neighbors.append(pixArray[width][height+1])

while running:

    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_RETURN) or event.type == QUIT:
            running = False

    update_cell(0, 19)

##    while go:
##        for i in range(1, screen_rect.height - 1):
##            pix_array = pygame.surfarray.pixels2d(background) 
##            for j in range(1, screen_rect.width - 1):
##                update_cell(i, j)
##                       
##                for event in pygame.event.get():
##                    if (event.type == KEYDOWN and event.key == K_RETURN) or event.type == QUIT:
##                        pygame.quit()
##
##            del pix_array
##            screen.blit(background, (0,0))
##            pygame.display.update()
##      go = False
pygame.quit()
