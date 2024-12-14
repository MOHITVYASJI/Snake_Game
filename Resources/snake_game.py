import pygame
from pygame.locals import *
#import time

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((1000,500))
    # time.sleep(10)
    surface.fill((160, 217, 192))
    pygame.display.flip()
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False