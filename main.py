import sys
from pygame.locals import QUIT, MOUSEBUTTONDOWN
import pygame
import buttons


pygame.init()
pygame.font.init()


WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)
GREEN  = pygame.Color(0, 255, 0)


window = pygame.display.set_mode((600, 600))
window.fill(WHITE)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        pygame.display.flip()


main()