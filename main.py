from importlib.resources import path
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


window = pygame.display.set_mode((600, 650))
pygame.display.set_caption("Algorithm Visualizer")
icon = pygame.image.load("Sprites/Icon.png")
pygame.display.set_icon(icon)
window.fill(WHITE)
title = pygame.font.SysFont("palatino linotype", 56, True)
back_button = buttons.Button(sprite="Sprites/Buttons/Back.png",
                             name="home", size=(150,75))
start_button = buttons.Button(sprite="Sprites/Buttons/Start.png",
                             name="start", size=(150,75))


def main():
    screen = pygame.Surface(window.get_size())
    screen.fill(WHITE)

    banner = title.render("Algorithm Visualizer", True, RED)
    banner_x = center(banner, screen)
    
    sort_button = buttons.Button(sprite="Sprites/Buttons/Home Screen/Sort.png",
                                 func=sort_screen)
    sort_x = center(sort_button.sprite, screen)
    path_find = buttons.Button(sprite="Sprites/Buttons/Home Screen/Path.png",
                               func=path_screen)
    path_x = center(path_find.sprite, screen)
    screen_buttons = [sort_button, path_find]

    screen.blit(banner, (banner_x, 50))
    sort_button.draw(screen, (sort_x, 175))
    path_find.draw(screen, (path_x, 375))
    window.blit(screen, (0,0))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                clicked_button = buttons.clicked(screen_buttons, event.pos)
                if clicked_button is not None:
                    clicked_button.click()
                    window.blit(screen, (0,0))

        pygame.display.flip()


def sort_screen():
    screen = pygame.Surface(window.get_size())
    screen.fill(WHITE)

    banner = title.render("Select Sort Type", True, RED)
    banner_x = center(banner, screen)

    sort_type = [(bubble, "Bubble Sort"), (select, "Selection Sort"),
                 (insert, "Insertion Sort"), (quick, "Quick Sort")]
    screen_buttons = [back_button]
    for i in range(4):
        button = buttons.Button(sprite=f"Sprites/Buttons/Sorts/{i}.png",
                                func=sort_visual, click_args=sort_type[i],
                                size=(200,100))
        button_x = center(button.sprite, screen)
        button.draw(screen, (button_x, 125 + (125*i)))
        screen_buttons.append(button)

    back_button.draw(screen, (440, 565))
    screen.blit(banner, (banner_x, 50))
    window.blit(screen, (0,0))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                clicked_button = buttons.clicked(screen_buttons, event.pos)
                if clicked_button is not None:
                    if clicked_button.name == "home":
                        return
                    else:
                        clicked_button.click()
                        window.blit(screen, (0, 0))
    
        pygame.display.flip()
    

def path_screen():
    screen = pygame.Surface(window.get_size())
    screen.fill(WHITE)

    banner = title.render("Coming Soon", True, RED)
    banner_x = center(banner, screen)

    back_button.draw(screen, (440, 565))
    screen.blit(banner, (banner_x, 50))
    window.blit(screen, (0,0))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                clicked_button = buttons.clicked(back_button, event.pos)
                if clicked_button is not None:
                    if clicked_button.name == "home":
                        return
                    else:
                        break
    
        pygame.display.flip()


def center(surf_to_draw: pygame.Surface, surf: pygame.Surface) -> int:
    """Returns an integer representing an x coordinate that will place 
       surf_to_draw in the center of surf if the left side of surf_to_draw is 
       placed at x"""
    w1 = surf.get_width()
    w2 = surf_to_draw.get_width()
    return (w1//2) - (w2//2)


def sort_visual(sort_func, sort_name):
    screen = pygame.Surface(window.get_size())
    screen.fill(WHITE)

    banner = title.render(sort_name, True, RED)
    banner_x = center(banner, screen)

    screen_buttons = [start_button, back_button]
    start_button.draw(screen, (280, 565))
    back_button.draw(screen, (440, 565))
    screen.blit(banner, (banner_x, 50))
    window.blit(screen, (0,0))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                clicked_button = buttons.clicked(screen_buttons, event.pos)
                if clicked_button is not None:
                    if clicked_button.name == "home":
                        return
                    else:
                        sort_func()

        pygame.display.flip()


def bubble():
    print("bubble")
    

def select():
    print("select")


def insert():
    print("insert")


def quick():
    print("quick")


main()