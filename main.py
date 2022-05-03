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
title = pygame.font.SysFont("palatino linotype", 56, True)
home_button = buttons.Button(sprite="Sprites/Home.png", name="home", size=(150,75))


def main():
    screen = pygame.Surface(window.get_size())
    screen.fill(WHITE)

    banner = title.render("Algorithm Visualizer", True, RED)
    banner_x = center(banner, screen)
    
    sort_button = buttons.Button(sprite="Sprites/Sort.png", func=sort_screen)
    sort_x = center(sort_button.sprite, screen)
    path_find = buttons.Button(sprite="Sprites/Path.png", func=path_screen)
    path_x = center(path_find.sprite, screen)

    screen.blit(banner, (banner_x, 50))
    sort_button.draw(screen, (sort_x, 175))
    path_find.draw(screen, (path_x, 375))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                clicked_button = buttons.clicked([sort_button, path_find], event.pos)
                if clicked_button is not None:
                    clicked_button.click()

        window.blit(screen, (0,0))
        pygame.display.flip()


def sort_screen():
    screen = pygame.Surface(window.get_size())
    screen.fill(WHITE)

    banner = title.render("Select Sort Type", True, RED)
    banner_x = center(banner, screen)

    home_button.draw(screen, (425, 500))
    screen.blit(banner, (banner_x, 50))
    window.blit(screen, (0,0))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                clicked_button = buttons.clicked(home_button, event.pos)
                if clicked_button is not None:
                    if clicked_button.name == "home":
                        return

        pygame.display.flip()


def path_screen():
    screen = pygame.Surface(window.get_size())
    screen.fill(WHITE)

    banner = title.render("Select Path Finding", True, RED)
    banner_x = center(banner, screen)

    home_button.draw(screen, (425, 500))
    screen.blit(banner, (banner_x, 50))
    window.blit(screen, (0,0))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                clicked_button = buttons.clicked(home_button, event.pos)
                if clicked_button is not None:
                    if clicked_button.name == "home":
                        return

        pygame.display.flip()


def center(surf_to_draw: pygame.Surface, surf: pygame.Surface) -> int:
    """Returns an integer representing an x coordinate that will place 
       surf_to_draw in the center of surf if the left side of surf_to_draw is 
       placed at x"""
    w1 = surf.get_width()
    w2 = surf_to_draw.get_width()
    return (w1//2) - (w2//2)

    
main()