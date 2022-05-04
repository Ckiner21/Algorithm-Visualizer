from random import randint
import sys
import time
from pygame.locals import QUIT, MOUSEBUTTONDOWN
import pygame
import buttons


pygame.init()
pygame.font.init()
clock = pygame.time.Clock()


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
                             name="back", size=(150,75))
start_button = buttons.Button(sprite="Sprites/Buttons/Start.png",
                             name="start", size=(150,75))


def main():
    screen = pygame.Surface(window.get_size())
    screen.fill(WHITE)

    banner = title.render("Algorithm Visualizer", True, RED)
    banner_x = center(banner, screen)
    
    sort_button = buttons.Button(sprite="Sprites/Buttons/Home Screen/Sort.png",
                                 func=sort_menu)
    sort_x = center(sort_button.sprite, screen)
    path_find = buttons.Button(sprite="Sprites/Buttons/Home Screen/Path.png",
                               func=path_menu)
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


def sort_menu():
    screen = pygame.Surface(window.get_size())
    screen.fill(WHITE)

    banner = title.render("Select Sort Type", True, RED)
    banner_x = center(banner, screen)

    sort_type = [(bubble, "Bubble Sort"), (select, "Selection Sort"),
                 (insert, "Insertion Sort")]
    screen_buttons = [back_button]
    for i in range(3):
        button = buttons.Button(sprite=f"Sprites/Buttons/Sorts/{i}.png",
                                func=sort_visual, click_args=sort_type[i],
                                size=(250,125))
        button_x = center(button.sprite, screen)
        button.draw(screen, (button_x, 110 + (175*i)))
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
                    if clicked_button.name == "back":
                        return
                    else:
                        clicked_button.click()
                        window.blit(screen, (0, 0))
    
        pygame.display.flip()
    

def path_menu():
    screen = pygame.Surface(window.get_size())
    screen.fill(WHITE)

    banner = title.render("Select an algorithm", True, RED)
    banner_x = center(banner, screen)

    dj_button = buttons.Button(func=path_visual, click_args=[djikstra, "Djikstra"],
                              sprite="Sprites/Buttons/Paths/Djikstra.png")
    djik_x = center(dj_button.sprite, screen)
    ast_button = buttons.Button(func=path_visual, click_args=[astar, "A*"],
                              sprite="Sprites/Buttons/Paths/AStar.png")
    astar_x = center(ast_button.sprite, screen)
    screen_buttons = [back_button, dj_button, ast_button]

    dj_button.draw(screen, (djik_x, 175))
    ast_button.draw(screen, (astar_x, 375))
    back_button.draw(screen, (440, 565))
    screen.blit(banner, (banner_x, 50))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                clicked_button = buttons.clicked(screen_buttons, event.pos)
                if clicked_button is not None:
                    if clicked_button.name == "back":
                        return
                    else:
                        clicked_button.click()
        
        window.blit(screen, (0,0))
        pygame.display.flip()


def sort_visual(sort_func, sort_name):
    screen = pygame.Surface(window.get_size())
    screen.fill(WHITE)

    banner = title.render(sort_name, True, RED)
    banner_x = center(banner, screen)

    pygame.draw.line(screen, BLACK, (0, 550), 
                    (screen.get_width(), 550),
                     width=1)
    pygame.draw.line(screen, BLACK, (0, 100), 
                    (screen.get_width(), 100),
                     width=1)             

    screen_buttons = [start_button, back_button]
    start_button.draw(screen, (290, 565))
    back_button.draw(screen, (440, 565))
    screen.blit(banner, (banner_x, 50))
    window.blit(screen, (0,0))

    array = make_array()
    for i, val in enumerate(array):
        pygame.draw.line(screen, BLACK,
                         (50+i, 550), (50+i, 550-val))
    started = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                clicked_button = buttons.clicked(screen_buttons, event.pos)
                if clicked_button is not None:
                    if clicked_button.name == "back":
                        return
                    elif not started:
                        sort_update = sort_func(array)
                        started = True

        if started:
            changes = next(sort_update)
            if changes == 1:
                started = False
                continue
            for i in changes[:2]:
                pygame.draw.line(screen, WHITE,
                         (50+i, 550), (50+i, 101))
                pygame.draw.line(screen, BLACK,
                         (50+i, 550), (50+i, 550-array[i]))
            time = title.render(f"Time: {round(changes[2], 2)}", True, RED, WHITE)
            screen.blit(time, (1, 575))

        window.blit(screen, (0,0))
        pygame.display.flip()


def bubble(array):
    s = time.time()
    for i in range(len(array)):
        sorted = True
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                sorted = False
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp
                yield (j, j+1, time.time()-s)

        if sorted:
            break
    
    yield 1


def select(array):
    s = time.time()
    for i in range(len(array)):
        minimum = i
        for j in range(i+1, len(array)):
            if array[j] < array[minimum]:
                minimum = j
        tmp = array[minimum]
        array[minimum] = array[i]
        array[i] = tmp
        yield(i, minimum, time.time()-s)
    
    yield 1


def insert(array):
    s = time.time()
    for i in range(1, len(array)):
        ptr = i
        while array[ptr] < array[ptr-1] and ptr != 0:
            tmp = array[ptr]
            array[ptr] = array[ptr-1]
            array[ptr-1] = tmp
            ptr -= 1
            yield(ptr, ptr+1, time.time()-s)
    
    yield 1


def make_array():
    array = [_ for _ in range(1,450)]
    # This number was found through trial and error
    # leaves no resemblance of being previously sorted
    for _ in range(800):  
        index1 = randint(0, 448)
        index2 = randint(0, 448)
        tmp = array[index1]
        array[index1] = array[index2]
        array[index2] = tmp
    
    return array


def path_visual(path_alg, name):
    screen = pygame.Surface(window.get_size())
    screen.fill(WHITE)
    colors = [GREEN, RED]

    banner = title.render(name, True, RED)
    banner_x = center(banner, screen)

    banner = title.render(name, True, RED)
    banner_x = center(banner, screen)
        
    begin = buttons.Button(sprite="Sprites/Buttons/Begin.png",
                           name="Begin", size=(75,75))
    end = buttons.Button(sprite="Sprites/Buttons/End.png",
                         name="End", size=(75,75))
    begin.draw(screen, (25, 565))
    end.draw(screen, (125, 565))
    start_button.draw(screen, (250, 565))
    back_button.draw(screen, (440, 565))
    screen.blit(banner, (banner_x, 50))
    screen_buttons = [start_button, back_button, begin, end]

    for i in range(1,25):
        pygame.draw.line(screen, BLACK, (75 + (18*i), 110), (75 + (18*i), 560))
        pygame.draw.line(screen, BLACK, (75, 110 + (18*i)), (525, 110 + (18*i)))
    window.blit(screen, (0,0))

    grid = []
    selecting = [False, None]
    end_points = [None, None]
    started = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                clicked_button = buttons.clicked(screen_buttons, event.pos)
                if clicked_button is not None:
                    if clicked_button.name == "back":
                        return
                    elif clicked_button.name == "start" and not started \
                            and None not in end_points:
                        started = True
                        path_update = path_alg(grid, end_points)
                    elif clicked_button.name == "Begin":
                        selecting = (True, 0)
                    elif clicked_button.name == "End":
                        selecting = (True, 1)
                elif selecting[0]:
                    slct_type = selecting[1]
                    cell = convert(event.pos)
                    if cell != -1:
                        old = end_points[slct_type]
                        if old is not None:  # Erase the previous cell for either start or finish location
                            rect = pygame.Rect(75 + (18*old[0]), 
                                               110 + (18*old[1]), 19, 19)
                            pygame.draw.rect(screen, WHITE, rect)
                            pygame.draw.rect(screen, BLACK, rect, 1)
                        end_points[slct_type] = cell  # Color in cell either red or green based off start or finishing
                        rect = pygame.Rect(75 + (18*cell[0]), 
                                           110 + (18*cell[1]), 18, 18)
                        pygame.draw.rect(screen, colors[slct_type], rect)
        # Draw border around grid, we do this at end because otherwise tile selection on edge is glitchy
        rect = pygame.Rect(75, 110, 450, 450)
        pygame.draw.rect(screen, BLACK, rect, 5)

        if started:
            print(next(path_update))

        window.blit(screen, (0, 0))
        pygame.display.flip()


def djikstra(grid, end_points):
    yield


def astar(grid):
    print("A Star")


def center(surf_to_draw: pygame.Surface, surf: pygame.Surface) -> int:
    """Returns an integer representing an x coordinate that will place 
       surf_to_draw in the center of surf if the left side of surf_to_draw is 
       placed at x"""
    w1 = surf.get_width()
    w2 = surf_to_draw.get_width()
    return (w1//2) - (w2//2)


def convert(mouse_pos):
    x, y = mouse_pos
    if x < 75 or x > 525 or y < 110 or y > 560:
        print("Out of box")
        return -1

    cell_x = (x-75)//18
    cell_y = (y-110)//18
    return (cell_x, cell_y)
    

main()