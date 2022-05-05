from random import randint
import sys
import time
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP
import pygame
import buttons


pygame.init()
pygame.font.init()
pygame.event.set_allowed([QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP])
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
    GREY = pygame.Color(38, 50, 56)
    ORANGE = pygame.Color(245, 179, 66)
    PURPLE = pygame.Color(150, 0 , 143)
    cell_colors = [GREEN, RED, GREY]

    banner = title.render(name, True, RED)
    banner_x = center(banner, screen)
    screen.blit(banner, (banner_x, 50))
    
    begin = buttons.Button(sprite="Sprites/Buttons/Begin.png",
                           name="Begin", size=(50,50))
    end = buttons.Button(sprite="Sprites/Buttons/End.png",
                         name="End", size=(50,50))
    block = buttons.Button(sprite="Sprites/Buttons/Block.png",
                           name="Block", size=(50,50))
    begin.draw(screen, (25, 575))
    end.draw(screen, (100, 575))
    block.draw(screen, (175, 575))
    start_button.draw(screen, (250, 565))
    back_button.draw(screen, (440, 565))
    screen_buttons = [start_button, back_button, begin, end, block]

    for i in range(1,25):
        pygame.draw.line(screen, BLACK, (75 + (18*i), 110), (75 + (18*i), 560))
        pygame.draw.line(screen, BLACK, (75, 110 + (18*i)), (525, 110 + (18*i)))
    window.blit(screen, (0,0))

    started = False
    blocking = False
    path = None
    is_selecting = [False, None]
    end_points = [None, None]
    grid = make_grid()
    
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
                        started = True  # Preventing user from editing grid while calculating
                        path = path_alg(grid, end_points)
                    elif clicked_button.name == "Begin" and not started:
                        is_selecting = (True, 0)
                        blocking = False
                    elif clicked_button.name == "End" and not started:
                        is_selecting = (True, 1)
                        blocking = False
                    elif not started:
                        is_selecting = (True, 2)

                elif is_selecting[0] and not started:
                    slct_type = is_selecting[1]
                    if slct_type == 2:
                        blocking = True
                    else:
                        cell = convert(event.pos)
                        if cell != -1:  # Make sure we are actually choosing a cell
                            old = end_points[slct_type]
                            if old is not None:  # Erase the previous cell for either start or finish location
                                color_cell(old, WHITE, screen)
                            end_points[slct_type] = cell
                            color_cell(cell, cell_colors[slct_type], screen)
                            grid[cell[1]][cell[0]] = [float('inf'), None, False, False]  # Allows you to use start and end points to erase blocks

            elif event.type == MOUSEBUTTONUP:
                blocking = False

        if started:
            visited = next(path)
            if type(visited) == tuple:
                color_cell(visited, ORANGE, screen)
            else:
                for i in visited:
                    color_cell(i, PURPLE, screen)
                started = False
        elif blocking:
            cell = convert(event.pos)
            if cell != -1:
                color_cell(cell, cell_colors[2], screen)
                grid[cell[1]][cell[0]][3] = True
        # Draw border around grid, we do this at end because otherwise tile selection on edge is glitchy
        rect = pygame.Rect(75, 110, 450, 450)
        pygame.draw.rect(screen, BLACK, rect, 5)

        window.blit(screen, (0, 0))
        pygame.display.flip()
        clock.tick(200)

def djikstra(grid, end_points):
    start, end = end_points
    has_path = True
    grid[start[1]][start[0]] = [0, None, False, False]

    curr = start
    while curr != end:
        grid[curr[1]][curr[0]][2] = True  # Visit the current
        distance = grid[curr[1]][curr[0]][0]
        # For all surrounding nodes, set new distance if needed
        if curr[1] != 0:
            if distance + 1 < grid[curr[1]-1][curr[0]][0]: 
                grid[curr[1]-1][curr[0]][0] = distance + 1
                grid[curr[1]-1][curr[0]][1] = curr
           
        if curr[0] != 0:
            if distance + 1 < grid[curr[1]][curr[0]-1][0]: 
                grid[curr[1]][curr[0]-1][0] = distance + 1
                grid[curr[1]][curr[0]-1][1] = curr

        if curr[1] != 24:
            if distance + 1 < grid[curr[1]+1][curr[0]][0]: 
                grid[curr[1]+1][curr[0]][0] = distance + 1
                grid[curr[1]+1][curr[0]][1] = curr
           
        if curr[0] != 24:
            if distance + 1 < grid[curr[1]][curr[0]+1][0]: 
                grid[curr[1]][curr[0]+1][0] = distance + 1
                grid[curr[1]][curr[0]+1][1] = curr

        yield curr
        #Calculate next shortest that isnt visited
        minimum = (float('inf'), None)
        for row in range(len(grid)):
            for col in range(len(grid)):
                to_be_checked = grid[row][col]
                if to_be_checked[2] == False and to_be_checked[0] < minimum[0] \
                        and to_be_checked[3] == False:
                    minimum = (to_be_checked[0], (col, row))

        if minimum[1] is None:
            has_path = False
            break
        curr = minimum[1]

    path = []
    if has_path:
        curr = grid[end[1]][end[0]][1]
        while curr != start:
            path.append(curr)
            previous = grid[curr[1]][curr[0]][1]
            curr = previous

    yield path


def astar(grid):
    print("A Star")


def convert(mouse_pos):
    x, y = mouse_pos
    if x < 75 or x >= 525 or y < 110 or y >= 560:
        return -1

    cell_x = (x-75)//18
    cell_y = (y-110)//18
    return (cell_x, cell_y)


def color_cell(cell, color, screen):
    rect = pygame.Rect(75 + (18*cell[0]), 110 + (18*cell[1]), 19, 19)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 1)


def make_grid():
    grid = []
    for i in range(25):
        row = []
        for j in range(25):
            row.append([float('inf'), None, False, False])  # Distance, node taken to get there, visited, blocked
        grid.append(row)
    
    return grid


def center(surf_to_draw: pygame.Surface, surf: pygame.Surface) -> int:
    """Returns an integer representing an x coordinate that will place 
       surf_to_draw in the center of surf if the left side of surf_to_draw is 
       placed at x"""
    w1 = surf.get_width()
    w2 = surf_to_draw.get_width()
    return (w1//2) - (w2//2)
    

main()