from importlib.resources import path
import sys
from turtle import home
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
pygame.display.set_caption("Algorithm Visualizer")
icon = pygame.image.load("Sprites/Icon.png")
pygame.display.set_icon(icon)
window.fill(WHITE)


def main():
    home_screen = pygame.Surface(window.get_size())
    home_screen.fill(WHITE)

    title = pygame.font.SysFont("palatino linotype", 56, True)
    title = title.render("Algorithm Visualizer", True, RED)
    title_x = center(title, home_screen)
    
    sort_button = buttons.Button(sprite="Sprites/Sort.png", func=sort_screen)
    sort_x = center(sort_button.sprite, home_screen)
    path_find = buttons.Button(sprite="Sprites/Path.png", func=path_screen)
    path_x = center(path_find.sprite, home_screen)

    home_screen.blit(title, (title_x, 50))
    sort_button.draw(home_screen, (sort_x, 175))
    path_find.draw(home_screen, (path_x, 375))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                clicked_button = buttons.clicked([sort_button, path_find], event.pos)
                if clicked_button is not None:
                    clicked_button.click()

        window.blit(home_screen, (0,0))
        pygame.display.flip()


def sort_screen():
    print('sort')


def path_screen():
    print('path')


def center(surf_to_draw: pygame.Surface, surf: pygame.Surface) -> int:
    """Returns an integer representing an x coordinate that will place 
       surf_to_draw in the center of surf if the left side of surf_to_draw is 
       placed at x"""
    w1 = surf.get_width()
    w2 = surf_to_draw.get_width()
    return (w1//2) - (w2//2)

    
main()