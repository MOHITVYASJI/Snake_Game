import pygame
from pygame.locals import *
#import time

def draw_block():
    surface.fill((160, 217, 192))
    surface.blit(block,(block_x,block_y))
    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((1000,500))
    # time.sleep(10)
    surface.fill((160, 217, 192))

    block = pygame.image.load("D:\C and C++ programing\Python\End_to_End_Games\snakebody.jpg").convert()
    block_x = 100
    block_y = 100
    surface.blit(block,(block_x,block_y))



    pygame.display.flip()
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False